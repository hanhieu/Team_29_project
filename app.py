import logging

import chainlit as cl
from bot.handlers.onboarding import ask_user_type
from bot.router import route

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
# Suppress noisy third-party loggers
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("watchfiles").setLevel(logging.WARNING)
logging.getLogger("chainlit").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.WARNING)


@cl.on_chat_start
async def on_chat_start():
    await ask_user_type()


@cl.on_message
async def on_message(message: cl.Message):
    await route(message)
