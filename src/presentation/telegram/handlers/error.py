from aiogram import Router, F
from aiogram.types import ErrorEvent, Message

from aiogram.filters import ExceptionTypeFilter

from src.common.applications.exceptions import ApplicationError

error_router = Router()

@error_router.error(ExceptionTypeFilter(ApplicationError), F.update.message.as_("message"))
async def handle_my_custom_exception(event: ErrorEvent, message: Message):
    await message.answer(event.exception.message())
