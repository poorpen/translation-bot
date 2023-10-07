from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.adapters.translator import DeepLTranslator

from .database import DatabaseMiddleware
from .translator import TranslatorMiddleware
from .identity_provider import IdentityProviderMiddleware
from .director import DirectorMiddleware
from .user import UserMiddleware


def setup_middlewares(
        dispatcher: Dispatcher,
        session_factory: async_sessionmaker,
        translator: DeepLTranslator
) -> None:
    dispatcher.message.middleware(DatabaseMiddleware(session_factory))
    dispatcher.message.middleware(TranslatorMiddleware(translator))
    dispatcher.message.middleware(IdentityProviderMiddleware())
    dispatcher.message.middleware(DirectorMiddleware())
    dispatcher.message.middleware(UserMiddleware())
