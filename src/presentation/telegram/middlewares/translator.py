from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.adapters.translator import DeepLTranslator


class TranslatorMiddleware(BaseMiddleware):

    def __init__(self, translator: DeepLTranslator):
        self._translator = translator

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        data["translator"] = self._translator
        return await handler(event, data)
