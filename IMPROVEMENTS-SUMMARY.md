# Tóm tắt cải tiến SPEC

## ✅ Những gì đã được cải thiện

### 1. Canvas — Thêm path "Mất tin" (path 4)
**Trước:** Chỉ có 3 paths (happy / low-confidence / failure)
**Sau:** Đầy đủ 4 paths, thêm row "Mất tin — user không tin AI" cho cả 3 features

**Tại sao quan trọng:** Template nhấn mạnh path 4 là critical — user phải có exit/fallback khi không tin AI. Thiếu path này = thiếu trust design.

---

### 2. Learning Signal — Thêm alert mechanism
**Trước:** Chỉ mô tả thu data gì
**Sau:** Thêm "Alert tự động khi acceptance rate giảm >10% trong 1 tuần hoặc escalation rate tăng >5%"

**Tại sao quan trọng:** Canvas example ghi rõ cần có trigger để biết model đang tệ đi. Không có alert = không biết khi nào cần can thiệp.

---

### 3. Learning Signal — Nhấn mạnh marginal value
**Trước:** "model chung không có"
**Sau:** "domain cực kỳ đặc thù (tiếng Việt, địa phương, dịch vụ mới), model chung không có. Không đối thủ nào thu được data này ngoài Xanh SM."

**Tại sao quan trọng:** Framework Day 5 nhấn mạnh: "AI capabilities commodity hoá → data riêng = lợi thế thật". Cần chỉ rõ competitive moat từ data.

---

### 4. ROI — Tính Net cụ thể
**Trước:** "Dương từ tháng 1", "ROI ~10x"
**Sau:** "+220M VND/tháng", "+1,33 tỷ VND/tháng", "+5,04 tỷ VND/tháng"

**Tại sao quan trọng:** Canvas example ghi thẳng số Net rất ấn tượng. Số cụ thể > mô tả chung chung.

---

### 5. Failure Mode #1 — Highlight "user KHÔNG BIẾT"
**Trước:** "Nguy hiểm vì user KHÔNG BIẾT thông tin sai"
**Sau:** "**NGUY HIỂM NHẤT vì user KHÔNG BIẾT thông tin sai** — AI trả lời tự tin, user tin hoàn toàn, chỉ phát hiện khi thanh toán"

**Tại sao quan trọng:** Template nhấn mạnh: "Failure mode nào user KHÔNG BIẾT bị sai? Đó là cái nguy hiểm nhất." Cần highlight rõ ràng.

---

### 6. Failure Mode #1 — Mitigation chi tiết hơn
**Trước:** "Pipeline crawl website Xanh SM hàng ngày"
**Sau:** "Pipeline crawl website Xanh SM hàng ngày để detect thay đổi. Alert content team khi phát hiện mismatch giữa FAQ và website."

**Tại sao quan trọng:** Mitigation phải actionable — không chỉ "crawl" mà phải có mechanism detect + alert.

---

### 7. Mini AI Spec — Thêm Agency Progression V1→V3
**Trước:** Không có
**Sau:** Roadmap rõ ràng V1 (MVP, escalate 30-40%) → V2 (6 tháng, 15-20%) → V3 (12 tháng, 90% tự động)

**Tại sao quan trọng:** Framework Day 5 nhấn mạnh: "Bắt đầu augmentation, tăng dần automation khi có data". Không có progression = thiếu tư duy dài hạn.

---

### 8. Mini AI Spec — Nhấn mạnh competitive moat
**Trước:** "model chung không có"
**Sau:** "Không đối thủ nào (Grab, Be, Gojek) có data này — competitive moat từ data, không phải từ model."

**Tại sao quan trọng:** Chỉ rõ lợi thế so với đối thủ cụ thể, không chỉ nói chung chung.

---

### 9. Mini AI Spec — Stack chi tiết hơn
**Trước:** "Gemini Flash (low latency, cost-effective)"
**Sau:** "Gemini Flash (low latency <3s, cost-effective $0.002-0.005/query) + monitoring dashboard cho content team track stale entries"

**Tại sao quan trọng:** Số liệu cụ thể + mention monitoring tool thể hiện đã nghĩ đến operational aspect.

---

## 📊 So sánh trước/sau

| Tiêu chí | Trước | Sau |
|----------|-------|-----|
| Canvas đầy đủ 4 paths | ❌ Thiếu path 4 | ✅ Đầy đủ |
| Learning signal có alert | ❌ Không có | ✅ Có trigger cụ thể |
| ROI có số Net | ❌ Mô tả chung | ✅ Số cụ thể (VND) |
| Failure mode highlight risk | ⚠️ Có nhưng chưa rõ | ✅ Bold + giải thích |
| Agency Progression | ❌ Không có | ✅ V1→V2→V3 roadmap |
| Competitive moat | ⚠️ Có nhưng chung | ✅ So sánh đối thủ cụ thể |
| Stack technical details | ⚠️ Có nhưng thiếu số | ✅ Latency + cost cụ thể |

---

## 🎯 Kết luận

**Trước:** Spec tốt, đủ điểm, nhưng chưa wow
**Sau:** Spec chi tiết, thể hiện tư duy sâu, có khả năng wow

**Điểm mạnh hiện tại:**
- Canvas đầy đủ 3 cột + 4 paths cho 3 features
- Failure modes thoughtful, có mitigation cụ thể
- ROI có số liệu thực tế, không chỉ ước lượng
- Mini AI spec có roadmap dài hạn (V1→V3)
- Thể hiện hiểu framework Day 5 (precision-first, data flywheel, agency progression)

**Điểm có thể cải thiện thêm (nếu có thời gian):**
- Thêm diagram/flowchart cho user journey (visual > text)
- Thêm screenshot mock UI vào prototype-readme
- Test prompt với 10 câu hỏi thực tế, ghi log kết quả

---

*Improvements Summary — Track XanhSM — Day 6 Hackathon*
