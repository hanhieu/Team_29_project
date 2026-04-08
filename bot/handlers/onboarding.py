import chainlit as cl


USER_TYPE_LABELS = {
    "nguoi_dung": "👤 Hành khách",
    "taxi": "🚖 Tài xế Taxi",
    "bike": "🛵 Tài xế Bike",
    "nha_hang": "🍜 Nhà hàng",
}


async def ask_user_type():
    actions = [
        cl.Action(name="set_type", value=key, label=label)
        for key, label in USER_TYPE_LABELS.items()
    ]
    await cl.Message(
        content="Xin chào! Bạn là ai? Vui lòng chọn loại tài khoản của bạn:",
        actions=actions,
    ).send()


@cl.action_callback("set_type")
async def on_set_type(action: cl.Action):
    user_type = action.value
    label = USER_TYPE_LABELS.get(user_type, user_type)
    cl.user_session.set("user_type", user_type)
    cl.user_session.set("history", [])
    await cl.Message(
        content=f"Đã xác nhận: **{label}**. Bạn có thể đặt câu hỏi ngay bây giờ!"
    ).send()
