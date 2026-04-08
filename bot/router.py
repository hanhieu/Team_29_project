import chainlit as cl
from bot.handlers.onboarding import ask_user_type
from bot.handlers.chat import handle_chat


async def route(message: cl.Message):
    user_type = cl.user_session.get("user_type")
    if not user_type:
        await ask_user_type()
        return
    await handle_chat(message.content, user_type)
