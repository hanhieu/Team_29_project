# Ngày Tổng Kết Phase 1 — Xanh SM AI Support Chatbot
**Nhóm:** 29 · **Track:** XanhSM  
**Chủ đề xuyên suốt cả ngày:** Chatbot AI hỗ trợ đa vai trò trong hệ sinh thái Xanh SM

---

## Mục tiêu cuối ngày

- Hoàn thành Worksheet 0–5
- Mini project proposal (5–7 slide hoặc 1-page proposal)
- Kết luận rõ ràng về deployment, cost, reliability và Track Phase 2
- Phiếu chấm peer review cho các đội trong zone

---

## Checklist chuẩn bị đầu ngày

- [ ] Nhóm đủ 4–6 thành viên
- [ ] Chủ đề đã chốt: **Chatbot AI hỗ trợ Xanh SM**
- [ ] Vai trò đã phân công: Product lead, Architect, Cost lead, Reliability lead, Presenter
- [ ] Nơi ghi chép chung đã sẵn sàng (giấy A3 hoặc file chung)

---

## Buổi sáng

---

### 08:00–08:15 | Khởi động & Mini Reflection

**Mỗi thành viên viết nhanh 3 ý:**

| | Học được nhiều nhất | Điểm yếu nhất | Hướng muốn đi sâu |
|---|---|---|---|
| TV1 | | | |
| TV2 | | | |
| TV3 | | | |
| TV4 | | | |

**Tổng hợp nhóm (3–5 ý):**

> _Điền sau khi thảo luận_

---

### Worksheet 0 — 08:15–08:40 | Learning Timeline

**Mục tiêu:** Xác định nhóm đã build được gì và chốt chủ đề phân tích production.

**2–3 kỹ năng nhóm tự tin nhất:**
1. RAG pipeline với ChromaDB + Vietnamese SBERT embedding
2. Tool calling / function calling với GPT-4o (tra cứu giá cước thực tế)
3. Intent classification + multi-turn conversation handling với Chainlit

**Mô tả sản phẩm đã làm:**

Chatbot AI hỗ trợ khách hàng Xanh SM — nền tảng xe điện (taxi + bike) của VinFast. Chatbot phục vụ 4 nhóm user: Hành khách, Tài xế Taxi, Tài xế Bike, Nhà hàng đối tác. Tích hợp RAG dual-search (ChromaDB), tool calling tra cứu giá cước 45 tỉnh thành, intent classifier (driver registration / human escalation / general), query rewriter, và guided form đăng ký tài xế.

**Câu hỏi bắt buộc:**

| Câu hỏi | Trả lời |
|---|---|
| Sản phẩm giải quyết bài toán gì? | Người dùng Xanh SM mất thời gian tìm thông tin giá cước, khu vực phục vụ, chính sách qua nhiều kênh rời rạc (website, hotline 1900 2088, mạng xã hội) — thông tin không phân loại theo vai trò. Chatbot trả lời tức thì (<3s), phân loại theo user role, thay thế hotline cho câu hỏi thông thường. |
| Ai là người dùng chính? | 4 nhóm: Hành khách (đặt xe, hỏi giá), Tài xế Taxi (chính sách, thu nhập, BHXH), Tài xế Bike (đăng ký, quyền lợi), Nhà hàng đối tác (onboarding, hoa hồng) |
| Vì sao phù hợp để phân tích deployment và cost? | Hệ thống đã có kiến trúc rõ ràng (RAG + LLM + tool calling), data thực tế (110+ Q&A + Facebook community data), và đang chạy được — đủ để phân tích production-readiness một cách cụ thể. |

---

### Worksheet 1 — 08:40–09:25 | Enterprise Deployment Clinic

**Mục tiêu:** Hiểu sự khác biệt giữa deploy demo và deploy enterprise.

**Bối cảnh tổ chức:**

Xanh SM là thương hiệu xe điện của VinFast/Vingroup — tập đoàn lớn với yêu cầu compliance cao, hệ thống IT nội bộ phức tạp, và dữ liệu khách hàng nhạy cảm (thông tin cá nhân tài xế, lịch sử chuyến đi, dữ liệu thanh toán).

**Dữ liệu hệ thống động đến:**

| Loại dữ liệu | Mức độ nhạy cảm | Ghi chú |
|---|---|---|
| Thông tin đăng ký tài xế (họ tên, SĐT, bằng lái) | 🔴 Cao — PII | Lưu trong `Dataset/driver_applications.json` |
| Lịch sử hội thoại chatbot | 🟡 Trung bình | Session-based, không persist lâu dài hiện tại |
| Feedback / correction log | 🟡 Trung bình | `data/feedback.jsonl` — cần audit trail |
| Giá cước (pricedata.json) | 🟢 Thấp | Thông tin công khai |
| FAQ knowledge base (qa.json) | 🟢 Thấp | Thông tin công khai |
| Facebook community data | 🟡 Trung bình | Cần xem xét ToS của Meta |

**3 ràng buộc enterprise lớn nhất:**

1. **Data residency & PII compliance:** Thông tin tài xế (họ tên, SĐT, bằng lái) là PII — phải lưu trong hạ tầng Việt Nam, không được gửi ra nước ngoài qua API bên thứ ba mà không có DPA (Data Processing Agreement). Hiện tại gọi OpenAI API → dữ liệu đi qua server Mỹ.

2. **Audit trail & traceability:** Vingroup yêu cầu log đầy đủ mọi interaction (ai hỏi gì, bot trả lời gì, khi nào) để phục vụ compliance và điều tra sự cố. Hệ thống hiện tại chỉ có `feedback.jsonl` — chưa đủ.

3. **Integration với hệ thống nội bộ:** Giá cước thực tế, trạng thái tài xế, lịch sử chuyến đi nằm trong hệ thống core của Xanh SM (không phải file JSON tĩnh). Cần API integration hoặc data sync pipeline để chatbot không bị stale.

**Lựa chọn deployment:**

☑ **Hybrid** — Cloud (LLM API) + On-prem (data & vector DB)

**2 lý do:**

1. LLM inference (GPT-4o) cần cloud vì không có GPU on-prem đủ mạnh để self-host model tương đương — nhưng PII data (thông tin tài xế, lịch sử chat) phải ở on-prem hoặc private cloud Việt Nam để đáp ứng yêu cầu data residency.
2. ChromaDB và knowledge base (FAQ + price data) nên chạy on-prem để giảm latency và tránh phụ thuộc internet cho mỗi query — chỉ gọi ra ngoài khi cần LLM inference.

**Gợi ý thảo luận:**

| Câu hỏi | Trả lời |
|---|---|
| Có cần audit trail không? | Có — mọi interaction cần log với timestamp, user_type, query, response, feedback |
| Dữ liệu có được rời khỏi tổ chức không? | Câu hỏi (không chứa PII) có thể gửi OpenAI. Thông tin tài xế KHÔNG được gửi ra ngoài. |
| Cần tích hợp hệ thống cũ không? | Có — cần sync giá cước và chính sách từ hệ thống core Xanh SM thay vì dùng file JSON tĩnh |
| Nếu trả lời sai thì ai bị ảnh hưởng đầu tiên? | Hành khách bị tính phí sai; Tài xế hiểu sai chính sách → vi phạm quy định → bị phạt/khóa tài khoản |

---

### Worksheet 2 — 09:35–10:15 | Cost Anatomy Lab

**Mục tiêu:** Bóc tách toàn bộ cost của hệ thống, không chỉ token/API.

**Ước lượng traffic:**

| Chỉ số | Conservative | Realistic | Optimistic |
|---|---|---|---|
| User/ngày | 500 | 3.000 | 10.000 |
| Request/ngày | 500 | 3.000 | 10.000 |
| Peak traffic | 50 req/giờ | 300 req/giờ | 1.000 req/giờ |
| Input tokens/request (avg) | ~800 tokens | ~800 tokens | ~800 tokens |
| Output tokens/request (avg) | ~300 tokens | ~300 tokens | ~300 tokens |

_Lưu ý: mỗi request thực ra gồm 3 LLM calls: intent detector (gpt-4o-mini, ~50 tokens), query rewriter (gpt-4o-mini, ~200 tokens), main chat (gpt-4o, ~1.100 tokens)_

**Bóc tách các lớp cost:**

| Lớp cost | Thành phần | Ước tính (Realistic) | Ghi chú |
|---|---|---|---|
| **Token / LLM API** | GPT-4o main chat | ~$18/ngày | 3.000 req × 1.100 tokens × $0.005/1K |
| | GPT-4o-mini intent + rewrite | ~$0.6/ngày | 3.000 req × 250 tokens × $0.0002/1K × 2 |
| **Compute** | Server chạy Chainlit app | ~$50–100/tháng | 1 VPS 4 vCPU / 8GB RAM |
| | ChromaDB (local) | $0 thêm | Chạy cùng server |
| **Storage** | Vector DB (ChromaDB) | ~$5/tháng | ~110 chunks, nhỏ |
| | Feedback + correction logs | ~$1/tháng | JSONL files |
| | Driver applications | ~$1/tháng | JSON files |
| **Embedding** | Vietnamese SBERT (local) | $0 | Self-hosted, chạy on-prem |
| **Human review** | Content team review correction | ~$200/tháng | 2h/tuần × 4 tuần × $25/h |
| | FAQ update & re-ingest | ~$100/tháng | 1h/tuần |
| **Logging & monitoring** | Log aggregation | ~$20/tháng | CloudWatch hoặc tương đương |
| **Maintenance** | Crawl pipeline (crawlFAQ.py) | ~$10/tháng | Cron job |
| | Dependency updates | ~$50/tháng | DevOps time |

**Tổng ước tính (Realistic):** ~$600–700/tháng

**Câu hỏi bắt buộc:**

| Câu hỏi | Trả lời |
|---|---|
| Cost driver lớn nhất? | GPT-4o token cost (~$540/tháng ở mức Realistic) — chiếm ~80% tổng cost |
| Hidden cost dễ bị quên nhất? | Human review (content team update KB) và maintenance pipeline crawl — không xuất hiện trong bill cloud nhưng tốn thực sự |
| Đang ước lượng quá lạc quan ở đâu? | Token count: system prompt dài (~800 tokens) + context RAG (~600 tokens) → thực tế input có thể 1.500–2.000 tokens/request, gấp đôi ước tính ban đầu |

**Khi scale 5x–10x:**

| Thành phần | Tăng tuyến tính? | Ghi chú |
|---|---|---|
| LLM API cost | ✅ Tuyến tính | Tăng đúng 5x–10x |
| Compute (server) | ⚠️ Bậc thang | Cần scale up/out khi vượt ngưỡng |
| ChromaDB | ✅ Gần tuyến tính | Nhưng query time tăng khi collection lớn |
| Human review | ⚠️ Không tuyến tính | Correction volume tăng nhưng team không tăng tương ứng |
| Embedding (SBERT) | ✅ Tuyến tính | CPU-bound, cần thêm instance |

---

### Worksheet 3 — 10:15–10:50 | Cost Optimization Debate

**Mục tiêu:** Chọn đúng chiến lược tối ưu, không tối ưu theo phong trào.

**3 chiến lược được chọn:**

#### Chiến lược 1: Semantic Caching
| | Chi tiết |
|---|---|
| **Tiết kiệm phần nào** | GPT-4o token cost — cache câu trả lời cho các câu hỏi tương tự (giá cước, FAQ phổ biến) |
| **Lợi ích** | Giảm 30–50% LLM calls cho FAQ lặp lại; latency gần 0 cho cached queries |
| **Trade-off** | Cache có thể stale nếu giá/chính sách thay đổi; cần TTL hợp lý (24h cho giá cước, 7 ngày cho FAQ ổn định) |
| **Thời điểm áp dụng** | Ngay — implement trước khi scale, ROI cao nhất ở giai đoạn đầu |

#### Chiến lược 2: Model Routing (gpt-4o-mini cho câu hỏi đơn giản)
| | Chi tiết |
|---|---|
| **Tiết kiệm phần nào** | 80–90% cost cho câu hỏi FAQ đơn giản (giá cước, giờ hoạt động, khu vực phục vụ) |
| **Lợi ích** | gpt-4o-mini rẻ hơn ~25x so với gpt-4o; đủ tốt cho câu hỏi có câu trả lời rõ ràng trong context |
| **Trade-off** | Cần classifier để phân loại câu hỏi đơn giản vs phức tạp; câu hỏi phức tạp (khiếu nại, tai nạn) vẫn cần gpt-4o |
| **Thời điểm áp dụng** | Sau khi có đủ data để train/eval classifier — Phase 2 |

#### Chiến lược 3: Prompt Compression
| | Chi tiết |
|---|---|
| **Tiết kiệm phần nào** | Input token cost — system prompt hiện tại ~800 tokens, có thể nén xuống ~400 tokens |
| **Lợi ích** | Giảm ~20% input tokens mà không ảnh hưởng chất lượng đáng kể |
| **Trade-off** | Cần test kỹ để đảm bảo không mất instruction quan trọng; một số rule có thể bị model bỏ qua khi prompt ngắn hơn |
| **Thời điểm áp dụng** | Ngay — low effort, high impact |

**Ưu tiên thực hiện:**

| Làm ngay | Để sau |
|---|---|
| Prompt compression (1–2 ngày, tiết kiệm ~20% cost) | Model routing (cần eval framework trước) |
| Semantic caching với TTL (1 tuần, tiết kiệm 30–50%) | Self-hosted model (cần đủ volume + GPU infra) |

---

### Worksheet 4 — 10:50–11:25 | Scaling & Reliability Tabletop

**Mục tiêu:** Luyện phản ứng khi hệ thống gặp tải tăng hoặc provider lỗi.

#### Tình huống 1: Traffic tăng đột biến (VD: Xanh SM chạy campaign khuyến mãi lớn)

| | Chi tiết |
|---|---|
| **Tác động tới user** | Response time tăng từ <3s lên 10–30s; một số request timeout; user bỏ chatbot, gọi hotline thay |
| **Phản ứng ngắn hạn** | Rate limiting per session (max 10 req/phút); queue request với async processing; hiển thị "Đang xử lý, vui lòng chờ..." |
| **Giải pháp dài hạn** | Horizontal scaling (multiple Chainlit instances + load balancer); semantic cache để giảm LLM calls; async queue (Celery/Redis) cho non-urgent requests |
| **Metric cần monitor** | p95 latency, request queue depth, error rate, OpenAI API rate limit hits |

#### Tình huống 2: OpenAI API timeout / outage

| | Chi tiết |
|---|---|
| **Tác động tới user** | Chatbot không trả lời được; user nhận error hoặc spinner vô tận |
| **Phản ứng ngắn hạn** | Retry với exponential backoff (3 lần, max 10s); sau đó fallback sang rule-based response cho FAQ phổ biến |
| **Giải pháp dài hạn** | Multi-provider fallback: OpenAI → Anthropic Claude → Azure OpenAI; circuit breaker pattern để không spam API khi đang lỗi |
| **Metric cần monitor** | OpenAI API error rate, fallback activation rate, MTTR (mean time to recovery) |

#### Tình huống 3: Response chậm / chất lượng thấp (RAG không tìm được context tốt)

| | Chi tiết |
|---|---|
| **Tác động tới user** | Bot trả lời chung chung, không đúng câu hỏi; user phải hỏi lại nhiều lần → frustration → escalation |
| **Phản ứng ngắn hạn** | Query rewriter đã có — tăng top_k từ 3 lên 5 để có nhiều context hơn; thêm confidence threshold để bot tự nhận "không tìm thấy thông tin" thay vì hallucinate |
| **Giải pháp dài hạn** | Cải thiện knowledge base (thêm Q&A, cập nhật thường xuyên); hybrid search (BM25 + vector); re-ranking layer |
| **Metric cần monitor** | RAG hit rate (% query có chunk score < threshold), escalation rate, thumbs-down rate |

**Fallback Proposal:**

```
Request đến
    ↓
Intent classifier (gpt-4o-mini, timeout 2s)
    ↓ timeout/error → fallback: "general"
RAG retrieval (ChromaDB local, timeout 1s)
    ↓ timeout/error → context = "(Không tìm thấy)"
GPT-4o main chat (timeout 8s)
    ↓ timeout/error → retry 1 lần
    ↓ vẫn lỗi → rule-based FAQ response (top 10 câu hỏi phổ biến)
    ↓ vẫn không match → "Xin lỗi, hệ thống đang bận. Hotline: 1900 2088"
```

**Các request nào cần real-time vs async:**

| Loại request | Real-time hay Async | Lý do |
|---|---|---|
| Hỏi giá cước | Real-time | User đang chuẩn bị đặt xe, cần ngay |
| Hỏi FAQ thông thường | Real-time | Kỳ vọng trả lời tức thì |
| Đăng ký tài xế (form submit) | Async OK | Lưu vào queue, xử lý sau, confirm qua SMS |
| Correction log (feedback) | Async | Không cần real-time, batch process hàng ngày |

---

### Worksheet 5 — 11:25–11:45 | Skills Map & Track Direction

**Mục tiêu:** Kết nối dự án với năng lực hiện tại và hướng đi Phase 2.

**Self-assessment (1–5):**

| Thành viên | Business/Product | Infra/Data/Ops | AI Engineering/Application |
|---|---|---|---|
| TV1 | | | |
| TV2 | | | |
| TV3 | | | |
| TV4 | | | |
| **Trung bình nhóm** | | | |

**Điểm mạnh của nhóm (dựa trên dự án đã làm):**
- AI Engineering: RAG pipeline, tool calling, intent classification, streaming — đã implement và chạy được
- Product: Canvas rõ ràng, user stories 4 path, eval metrics có threshold cụ thể

**Điểm cần bù:**
1. Infra/Ops: chưa có monitoring, logging đầy đủ, CI/CD pipeline
2. Data: knowledge base còn nhỏ (110 Q&A), chưa có pipeline crawl tự động chạy production
3. Cost optimization: chưa implement caching, chưa có model routing

**Track Phase 2 đề xuất:** ☑ **AI Engineering / Application**

Lý do: Nhóm đã có nền tảng kỹ thuật tốt (RAG + LLM + tool calling). Phase 2 nên đi sâu vào: (1) production hardening — monitoring, caching, fallback; (2) knowledge base expansion — crawl pipeline tự động, data flywheel từ feedback; (3) eval framework — automated testing cho precision/recall.

---

## Buổi chiều

---

### 13:30–13:45 | Chia zone và chốt vai trò

- [ ] Đã biết zone của nhóm
- [ ] Đã có presenter và người trả lời Q&A
- [ ] Đã thống nhất format: **Slide (5–7 slides)**

---

### 14:00–15:10 | Sprint 1 — Xây nội dung proposal

**7 khối nội dung cần hoàn thành:**

#### Khối 1: Project Overview
- **Tên:** Xanh SM AI Support Chatbot
- **User:** 4 nhóm — Hành khách, Tài xế Taxi, Tài xế Bike, Nhà hàng đối tác
- **Bài toán:** Thông tin rời rạc, không phân loại theo vai trò → hotline quá tải
- **AI giải:** Chatbot RAG + tool calling, trả lời tức thì <3s, phân loại theo user role

#### Khối 2: Enterprise Context
- Vingroup/VinFast — tập đoàn lớn, yêu cầu compliance cao
- PII: thông tin tài xế không được rời khỏi hạ tầng Việt Nam
- Cần audit trail đầy đủ
- Cần integration với hệ thống core (giá cước real-time, trạng thái tài xế)

#### Khối 3: Deployment Choice
- **Hybrid:** LLM API (cloud) + Data & Vector DB (on-prem/private cloud VN)
- Câu hỏi (không PII) → OpenAI API
- Thông tin tài xế, feedback, KB → on-prem
- ChromaDB + SBERT embedding chạy local → zero latency cho retrieval

#### Khối 4: Cost Analysis
- **MVP:** ~$200/tháng (500 req/ngày × $0.005/req × 30 + infra)
- **Realistic:** ~$700/tháng (3.000 req/ngày)
- **Cost driver:** GPT-4o token (~80% tổng cost)
- **Hidden cost:** Human review content team (~$300/tháng)

#### Khối 5: Optimization Plan
1. Prompt compression → tiết kiệm ~20% input tokens (làm ngay)
2. Semantic caching (TTL 24h cho giá cước) → giảm 30–50% LLM calls (làm ngay)
3. Model routing (gpt-4o-mini cho FAQ đơn giản) → giảm 80% cost cho simple queries (Phase 2)

#### Khối 6: Reliability Plan
- Fallback chain: GPT-4o → retry → rule-based FAQ → hotline 1900 2088
- Circuit breaker cho OpenAI API
- Rate limiting per session
- Monitor: p95 latency, escalation rate, thumbs-down rate, RAG hit rate

#### Khối 7: Track Recommendation
- **Track:** AI Engineering / Application
- **Next step Phase 2:**
  1. Implement semantic caching + model routing
  2. Xây eval framework tự động (precision/recall test suite)
  3. Crawl pipeline tự động cập nhật KB hàng ngày
  4. Monitoring dashboard (latency, cost, quality metrics)

---

### 15:20–16:00 | Sprint 2 — Cấu trúc slide đề xuất

| Slide | Nội dung |
|---|---|
| 1 | Tên dự án + tagline + 4 user groups + bài toán (1 câu) |
| 2 | Enterprise context: Vingroup constraints, PII, audit trail, integration needs |
| 3 | Kiến trúc hybrid: diagram flow từ user → intent → RAG → GPT-4o → response |
| 4 | Cost anatomy: bảng 3 kịch bản + cost driver breakdown (pie chart) |
| 5 | Cost optimization: 3 chiến lược + timeline làm ngay vs để sau |
| 6 | Reliability & scaling: fallback chain + 3 failure scenarios + metrics |
| 7 | Track Phase 2 + 4 next steps cụ thể + kill criteria |

---

### 16:10–17:20 | Zone Presentation + Peer Review

**Format mỗi đội:** 5 phút trình bày · 3 phút Q&A · 2 phút chấm phiếu

**Luật bắt buộc:**
- Không tự chấm mình
- Đặt ít nhất 1 câu hỏi thật cho ít nhất 2 đội khác
- Phản biện: 1 điểm mạnh + 1 điểm cần cải thiện + 1 đề xuất thay thế

---

## Checklist nộp cuối ngày

- [ ] Worksheet 0–5 (file này)
- [ ] Slide hoặc poster mini project (5–7 slides)
- [ ] Phiếu chấm cho các đội khác trong zone
- [ ] Kết luận Track Phase 2: **AI Engineering / Application**

---

## Team Note Sheet

| | |
|---|---|
| **Tên nhóm** | Nhóm 29 |
| **Chủ đề** | Xanh SM AI Support Chatbot |
| **3 ràng buộc enterprise lớn nhất** | 1. PII data residency (thông tin tài xế không rời VN) · 2. Audit trail đầy đủ · 3. Integration với hệ thống core Xanh SM |
| **Cost driver lớn nhất** | GPT-4o token cost (~80% tổng cost) |
| **3 chiến lược optimize** | 1. Prompt compression (làm ngay) · 2. Semantic caching TTL 24h (làm ngay) · 3. Model routing gpt-4o-mini (Phase 2) |
| **Fallback / reliability plan** | GPT-4o → retry → rule-based FAQ top 10 → hotline 1900 2088; circuit breaker + rate limiting |
| **Track Phase 2** | AI Engineering / Application — production hardening + eval framework + data flywheel |
