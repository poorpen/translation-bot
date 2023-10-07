from aiogram import Dispatcher

from .command import command_router
from .translator import translator_router
from .error import error_router


def setup_routers(dp: Dispatcher) -> None:
    dp.include_router(error_router)
    dp.include_router(command_router)
    dp.include_router(translator_router)
