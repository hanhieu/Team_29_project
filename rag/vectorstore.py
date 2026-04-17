import os

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from config import settings
CHROMA_PATH = settings.chroma_path
COLLECTION_NAME = settings.collection_name
EMBEDDING_MODEL = settings.embedding_model

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
os.environ.setdefault("TQDM_DISABLE", "1")

_collection = None


def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_PATH)
        embedding_fn = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
        _collection = client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_fn,
        )
    return _collection
