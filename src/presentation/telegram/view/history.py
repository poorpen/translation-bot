from datetime import tzinfo

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from src.application.translator.models.dto import TranslationHistoryDTO, TranslatedMessageDTO


async def render_history(bot_event: Message, data: TranslationHistoryDTO):
    text = ""
    for row in data.messages:
        text += (
            f"--------------------------------------------------------------\n"
            f"\n"
            f"Оригитальный текста (EN):\n"
            f"{row.original_text}\n"
            f"\n"
            f"Перевод (RU):\n"
            f"{row.translated_text}\n\n")
    if not text:
        text = "История сообщений пуста :("
    await bot_event.answer(text)


async def render_translate(bot_event: Message, data: TranslatedMessageDTO):
    await bot_event.answer(
        data.text,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="История переводов")]],
            resize_keyboard=True,

        )
    )
