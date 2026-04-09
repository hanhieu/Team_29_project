# AI Product Canvas — Xanh SM AI Support Chatbot

**Nhóm:** 29 · **Track:** XanhSM

---

## Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi guide** | User nào? Pain gì? AI giải quyết gì mà cách hiện tại không giải được? | Khi AI sai thì user bị ảnh hưởng thế nào? User biết AI sai bằng cách nào? User sửa bằng cách nào? | Cost bao nhiêu/request? Latency bao lâu? Risk chính là gì? |
| **Trả lời** | **User:** Hành khách Xanh SM — đặc biệt khách nước ngoài tại Việt Nam (du lịch, expat, công tác) và người dùng mới. Khách nước ngoài là nhóm dùng mobility nhiều nhất (không có xe riêng, không quen đường) nhưng được hỗ trợ kém nhất (hotline/website chủ yếu tiếng Việt). **Pain:** Mất 5–10 phút tìm thông tin giá cước, khu vực phục vụ, chính sách hoàn tiền qua nhiều kênh rời rạc (website, hotline 1900 2088, mạng xã hội). **AI giải:** Trả lời tức thì (<3s) bằng tiếng Anh/tiếng Việt, gợi ý đúng dịch vụ (Car / Premium / Bike / Express), cung cấp nút đặt xe ngay — thay thế hoàn toàn việc phải gọi hotline cho câu hỏi thông thường. | **Khi AI sai:** AI báo sai giá hoặc khu vực phục vụ → user đặt xe nhầm dịch vụ, bị tính phí sai. **User biết sai:** Disclaimer "Thông tin có thể thay đổi, xác nhận qua app khi đặt xe" hiển thị mỗi câu trả lời. Nút "Báo sai" 1 click luôn hiển thị. **User sửa:** Nhấn "Báo sai" + nhập thông tin đúng (tùy chọn) → correction log → content team review → cập nhật knowledge base. **Mất tin:** Nút "Gọi hotline 1900 2088" và "Chat với nhân viên" luôn hiển thị ở góc dưới — không bao giờ bị ẩn, user không bị lock-in. | **Cost:** ~$0.002–0.005/query (GPT-4o). **Latency:** <3s (streaming response). **Risk chính:** Thông tin giá/khuyến mãi thay đổi thường xuyên mà knowledge base chưa cập nhật kịp — user KHÔNG BIẾT bị sai vì AI trả lời tự tin. **Mitigation:** Timestamp mỗi FAQ entry, auto-disclaimer nếu entry >7 ngày chưa verify, pipeline crawl website Xanh SM hàng ngày. |

---

## Automation hay augmentation?

☑ Augmentation — AI gợi ý, user quyết định cuối cùng

**Justify:** AI trả lời câu hỏi + gợi ý dịch vụ, nhưng user tự quyết định có đặt xe không — cost of reject = 0. Thông tin giá/chính sách sai có hậu quả trực tiếp (user bị tính phí sai) nên không thể để AI tự động hóa hoàn toàn. Với câu hỏi phức tạp (khiếu nại, tai nạn), AI hard-route sang agent người thật — không tự xử lý.

---

## Learning signal

| # | Câu hỏi | Trả lời |
|---|---------|---------|
| 1 | User correction đi vào đâu? | Nút "Báo sai" + nội dung câu hỏi/câu trả lời → correction log → content team review hàng tuần → cập nhật knowledge base → model fine-tune theo chu kỳ 2 tuần |
| 2 | Product thu signal gì để biết tốt lên hay tệ đi? | **Implicit:** tỷ lệ user click nút dịch vụ sau chatbot (conversion rate). **Explicit:** thumbs up/down sau mỗi câu trả lời. **Correction:** user nhấn "Báo sai". **Alert tự động** khi acceptance rate giảm >10% trong 1 tuần hoặc escalation rate tăng >5% so với baseline. |
| 3 | Data thuộc loại nào? ☑ Domain-specific · ☑ Real-time · ☑ Human-judgment | FAQ Xanh SM + phản hồi cộng đồng về taxi điện VN là domain cực kỳ đặc thù (tiếng Việt, địa phương, dịch vụ mới) — model chung không có. Giá/khuyến mãi thay đổi real-time. Phân loại câu hỏi mạng xã hội cần human judgment. |

**Có marginal value không?** Có — không đối thủ nào (Grab, Be, Gojek) thu được data này. FAQ Xanh SM + phản hồi cộng đồng về xe điện VN là competitive moat từ data, không phải từ model. Mỗi interaction thêm → data flywheel → model tốt hơn → escalation rate giảm → tiết kiệm chi phí hotline.

