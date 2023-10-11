from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.adapters.identity_provider import TelegramIdentityProvider


class IdentityProviderMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        data["identity_provider"] = TelegramIdentityProvider(event.from_user)
        return await handler(event, data)
