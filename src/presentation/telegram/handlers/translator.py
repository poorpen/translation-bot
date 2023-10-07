from aiogram import Router, F
from aiogram.types import Message

from src.application.translator.models.command import TranslationMessage
from src.application.translator.models.query import GetHistory
from src.adapters.director import Director
from src.presentation.telegram.view.history import render_translate, render_history

translator_router = Router()


@translator_router.message(F.text.lower() == "история переводов")
async def get_history(message: Message, director: Director):
    history = await director.execute(GetHistory())
    await render_history(message, history)


@translator_router.message()
async def translate_message(message: Message, director: Director):
    translation = await director.execute(TranslationMessage(message.text))
    await render_translate(message, translation)
