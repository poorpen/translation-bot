from aiogram.types import Message


async def render_start_message(bot_event: Message):
    await bot_event.answer(
        "Привет! 👋 Добро пожаловать в мой переводчик! "
        "Я готов помочь тебе разговаривать на разных языках. "
        "Просто напиши мне фразу на английском, и я переведу её на русский. Давай начнем! 🌍✨"
    )
