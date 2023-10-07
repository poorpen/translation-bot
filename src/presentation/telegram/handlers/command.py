from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.presentation.telegram.view.start import render_start_message

command_router = Router()


@command_router.message(CommandStart())
async def start(message: Message):
    await render_start_message(message)
