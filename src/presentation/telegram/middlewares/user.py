from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.application.user.models.command import AddUser
from src.application.user.models.query import CheckExist


class UserMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        director = data["director"]
        if not await director.execute(CheckExist()):
            await director.execute(AddUser(
                event.from_user.username,
                event.from_user.first_name,
                event.from_user.last_name
            ))
        return await handler(event, data)
