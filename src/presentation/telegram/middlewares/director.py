from typing import Any, Dict, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.application.translator.models.command import TranslationMessage
from src.application.translator.models.query import GetHistory
from src.application.translator.commands import TranslateMessageCommand
from src.application.translator.queries import GetHistoryQuery

from src.application.user.models.command import AddUser
from src.application.user.models.query import CheckExist
from src.application.user.commands import AddUserCommand
from src.application.user.queries import CheckExistQuery
from src.adapters.director import Director


class DirectorMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> None:
        db_gateway = data["db_gateway"]
        identity_provider = data["identity_provider"]
        translator = data["translator"]

        director = Director()

        director.register_handler(
            TranslationMessage, TranslateMessageCommand(translator, db_gateway, identity_provider)
        )
        director.register_handler(
            AddUser, AddUserCommand(db_gateway, identity_provider)
        )
        director.register_handler(
            GetHistory, GetHistoryQuery(db_gateway, identity_provider)
        )
        director.register_handler(
            CheckExist, CheckExistQuery(db_gateway, identity_provider)
        )

        data["director"] = director
        return await handler(event, data)
