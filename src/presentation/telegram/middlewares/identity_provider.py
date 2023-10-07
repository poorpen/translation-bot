from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.adapters.identity_provider import IdentityProvider
from src.adapters.identity_provider.plugins import TelegramIdentifyPlugin


class IdentityProviderMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        data["identity_provider"] = IdentityProvider(TelegramIdentifyPlugin, event.from_user)
        return await handler(event, data)
