from typing import Tuple

from aiogram import Bot, Dispatcher

from src.adapters.database.connection import session_factory
from src.adapters.translator import DeepLTranslator

from src.presentation.telegram.middlewares import setup_middlewares
from src.presentation.telegram.handlers import setup_routers

from .config import Config


def parametrize_bot(config: Config) -> Tuple[Bot, Dispatcher]:
    session_maker = session_factory(config.db)
    translator = DeepLTranslator(config.translator)

    bot = Bot(config.bot.token)
    dp = Dispatcher()

    setup_middlewares(dp, session_maker, translator)
    setup_routers(dp)
    return bot, dp
