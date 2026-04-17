# ─────────────────────────────────────────────────────────────────────────────
# Stage 1: builder — install heavy dependencies + pre-download SBERT model
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

# System deps needed by sentence-transformers & chromadb
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages into a prefix (so we can copy just site-packages)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Pre-download the Vietnamese SBERT model (~400 MB) into the image
# This avoids a slow cold start in production
RUN python -c "\
from sentence_transformers import SentenceTransformer; \
SentenceTransformer('keepitreal/vietnamese-sbert', cache_folder='/install/sbert_cache')"

# ─────────────────────────────────────────────────────────────────────────────
# Stage 2: runtime — lean image, non-root user, ChromaDB pre-built
# ─────────────────────────────────────────────────────────────────────────────
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy installed packages + pre-downloaded model from builder
COPY --from=builder /install /usr/local

# Copy application source
COPY . .

# Set the model cache location (matches where builder downloaded it)
ENV SENTENCE_TRANSFORMERS_HOME=/usr/local/sbert_cache
ENV TRANSFORMERS_CACHE=/usr/local/sbert_cache

# Default environment (can be overridden by Railway / Render / docker-compose)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000 \
    HOST=0.0.0.0 \
    ENVIRONMENT=production \
    CHROMA_PATH=/app/.chromadb \
    FEEDBACK_PATH=/app/data/feedback.jsonl

# Pre-build the ChromaDB vector index from qa.json so the image is self-contained
# (Requires data/qa.json to be present in the build context)
RUN python rag/ingest.py && echo "ChromaDB index built successfully."

# Create non-root user for security (12-factor: process = stateless, run as non-root)
RUN useradd --system --create-home --uid 1001 appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE $PORT

# Docker HEALTHCHECK — platform will restart container if /health stops responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/health')" \
    || exit 1

# Start Chainlit server
# --host 0.0.0.0 is required for Railway/Render to receive external traffic
CMD chainlit run app.py --host $HOST --port $PORT --headless
