# Hackathon Day 6 — Checklist đầy đủ

**Nhóm:** ___
**Track:** XanhSM
**Product:** AI Support Chatbot

---

## ✅ Đã hoàn thành

- [x] **spec-final.md** — SPEC 6 phần đầy đủ
- [x] **prototype-readme.md** — Template sẵn, cần điền thông tin
- [x] **demo-script.md** — Template sẵn, cần phân công ai nói gì

---

## 📋 Cần làm tiếp (theo thứ tự ưu tiên)

### NGAY BÂY GIỜ (trước M1 — 9:00 sáng Day 6)

- [ ] **Điền tên nhóm** vào tất cả các file (spec-final.md, prototype-readme.md, demo-script.md)
- [ ] **Review spec-final.md** — đọc lại, sửa lỗi chính tả, đảm bảo logic nhất quán
- [ ] **Phân công rõ ràng** — ai làm gì, ghi vào prototype-readme.md
- [ ] **Chọn POC option** — Sketch / Mock / Working? Ghi vào prototype-readme.md

### SÁNG DAY 6 (9:00-13:00)

#### M1 — Canvas check (9:00)
- [ ] Có Canvas đầy đủ (Value / Trust / Feasibility + Learning signal) ✅
- [ ] GV check pass → vào build ngay

#### Build Prototype (9:15-11:00)
- [ ] **Nếu chọn Sketch:** Vẽ user journey trên giấy A3 — 3 màn hình chính (hỏi → trả lời → gợi ý dịch vụ)
- [ ] **Nếu chọn Mock:** Build UI bằng Claude Artifacts / Antigravity / Figma
- [ ] **Nếu chọn Working:** Code chatbot với Gemini API / GPT-4o-mini
- [ ] **BẮT BUỘC:** Có ít nhất 1 prompt/AI call chạy thật (dù chọn Sketch/Mock)

#### M2 — Checkpoint (11:00)
- [ ] Show được 1 thứ chạy (dù rough)
- [ ] Mỗi người nói được đang làm gì
- [ ] Biết sẽ demo flow nào

#### Build tiếp (11:15-13:00)
- [ ] Polish prototype
- [ ] Test prompt với 5-10 câu hỏi mẫu, ghi log kết quả
- [ ] Mỗi người commit ít nhất 1 lần lên repo nhóm

#### M3 — SPEC final (13:00 trước nghỉ trưa)
- [ ] SPEC đã final ✅
- [ ] Demo flow draft đã có (ghi vào demo-script.md)

### CHIỀU DAY 6 (14:00-16:00)

#### Polish + Chuẩn bị demo (14:00-15:30)
- [ ] **Viết demo script chi tiết** — ai nói gì, show gì, thứ tự nào (dùng demo-script.md)
- [ ] **Tạo demo slides/poster** — Problem → Solution → Auto/Aug → Demo (dùng Canva hoặc Google Slides)
- [ ] **Chuẩn bị backup** — screenshot hoặc video demo phòng internet chết
- [ ] **Mỗi người luyện trả lời 3 câu:**
  - "Auto hay augmentation? Tại sao?"
  - "Failure mode chính là gì?"
  - "Phần mình làm gì?"

#### M4 — Demo prep done (15:30)
- [ ] Dry run demo trong nhóm, bấm giờ (không quá 2 phút)
- [ ] Laptop mở sẵn demo, test internet
- [ ] Poster/slides in ra hoặc mở sẵn
- [ ] Feedback forms nhận đủ

### DEMO ROUND (16:00-17:00)

#### Chuẩn bị station
- [ ] 2-3 người ở lại demo tại bàn
- [ ] 2-3 người đi xem các team khác trong zone
- [ ] Poster/slides trưng bày rõ ràng

#### Khi demo
- [ ] Nói chậm, rõ ràng
- [ ] Show prototype chạy thật
- [ ] Trả lời câu hỏi peer tự tin
- [ ] Điền feedback cho các team đã xem (3 tiêu chí × 1-5 + 1 điều tốt + 1 gợi ý)

### SAU DEMO (17:00-23:59 Day 6)

#### Nộp bài nhóm (deadline 23:59)
- [ ] **Tạo repo nhóm public:** `NhomXX-Lop-Day06` (VD: Nhom01-403-Day06)
- [ ] **Push 3 file lên repo:**
  - spec-final.md
  - prototype-readme.md (đã điền đầy đủ)
  - demo-slides.pdf
- [ ] **Nộp link repo nhóm lên LMS** — mọi thành viên đều nộp link này

#### Nộp bài cá nhân (deadline 23:59)
- [ ] **Tạo repo cá nhân public:** `MaHocVien-HoTen-Day06` (VD: AI20K001-NguyenVanA-Day06)
- [ ] **Viết feedback.md** — feedback cho các team đã xem (3 tiêu chí + comment)
- [ ] **Viết reflection.md** — 7 phần:
  1. Role cụ thể trong nhóm
  2. Phần phụ trách cụ thể (2-3 đóng góp có output rõ)
  3. SPEC phần nào mạnh/yếu nhất? Vì sao?
  4. Đóng góp cụ thể khác
  5. 1 điều học được
  6. Nếu làm lại, đổi gì?
  7. AI giúp gì? AI sai/mislead ở đâu? (bắt buộc cả hai mặt)
- [ ] **Nộp link repo cá nhân lên LMS**

---

## ⚠️ Binary gates — TRÁNH

| Tình huống | Hậu quả |
|-----------|---------|
| Không nộp SPEC draft trước 23:59 D5 | -5 điểm |
| Prototype không có AI call thật | Cap Prototype ở 4/10 |
| Không giải thích được phần mình | 0 điểm Prototype cá nhân |
| Không có commit trên group repo | 0 tất cả điểm cá nhân |
| Không nộp đủ feedback forms | 0 điểm "nộp đủ" |
| Copy-paste reflection | 0 toàn bộ reflection |

---

## 💡 Tips để "wow"

### Trong SPEC
- [x] Canvas có đủ 4 paths (happy / low-confidence / failure / **mất tin**) ✅
- [x] ROI có số Net cụ thể (VD: +220M VND/tháng) ✅
- [x] Learning signal có alert mechanism ✅
- [x] Mini AI spec có Agency Progression V1→V3 ✅
- [x] Failure mode #1 highlight "user KHÔNG BIẾT" ✅

### Trong Demo
- [ ] Show prototype chạy thật (không chỉ nói)
- [ ] Chỉ rõ: AI trả lời từ đâu, confidence thế nào, user sửa bằng cách nào
- [ ] Mỗi người nói ít nhất 1 phần (không để 1 người nói hết)
- [ ] Có backup plan (screenshot/video) phòng demo crash

### Trong Feedback
- [ ] Comment cụ thể, không chấm bừa
- [ ] 1 điều làm tốt + 1 gợi ý cải thiện phải thực chất
- [ ] Nộp đủ feedback cho tất cả team trong zone

### Trong Reflection
- [ ] Không viết chung chung ("thành viên", "cố gắng hơn")
- [ ] Phải có output cụ thể (file nào, phần nào, commit nào)
- [ ] Phải nêu cả mặt tốt VÀ mặt sai của AI — không chỉ khen

---

## 📊 Scoring breakdown (tổng 100 điểm)

| Hạng mục | Điểm | Loại |
|----------|------|------|
| SPEC milestone | 25 | Nhóm (20) + cá nhân (5) |
| Prototype milestone | 15 | Nhóm (10) + cá nhân (5) |
| Demo Day | 25 | Nhóm (peer 15 + feedback quality 7 + bonus 3) |
| UX exercise | 10 | Cá nhân + bonus |
| Individual reflection | 25 | Cá nhân (role 10 + reflection 15) |
| **Tổng** | **100** | |

---

## 🔗 Links hữu ích

- Xanh SM website: https://www.xanhsm.com/
- Xanh SM FAQ: https://www.xanhsm.com/helps
- Google AI Studio (test Gemini): https://aistudio.google.com/
- Claude Artifacts: https://claude.ai/
- Canva (poster): https://www.canva.com/

---

*Checklist — Nhóm ___ — Track XanhSM — Day 6 Hackathon*
*VinUni A20 — AI Thực Chiến · 2026*
