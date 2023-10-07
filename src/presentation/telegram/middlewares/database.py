from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.adapters.database import DBGateway


class DatabaseMiddleware(BaseMiddleware):

    def __init__(self, session_factory: async_sessionmaker):
        self._session_factory = session_factory

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        async with self._session_factory() as session:
            data["db_gateway"] = DBGateway(session)
            return await handler(event, data)
