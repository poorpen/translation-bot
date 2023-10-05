from typing import Optional

from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from src.common.applications.exceptions import ApplicationError
from src.common.adapters.database.repositories.base import SQLAlchemyRepo
from src.common.adapters.database.exception_mapper import exception_mapper

from src.application.user.interfaces.repo import IUserRepo
from src.application.user.exceptions import UserAlreadyExists

from src.adapters.database.models.user.user import user_table


class UserRepo(SQLAlchemyRepo, IUserRepo):

    @exception_mapper
    async def add_user(
            self,
            telegram_id: int,
            username: Optional[str],
            first_name: str,
            last_name: Optional[str]
    ) -> None:
        stmt = insert(user_table).values(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        try:
            await self._session.execute(stmt)
        except IntegrityError as exc:
            self._error_parser(exc)

    @staticmethod
    def _error_parser(exc: IntegrityError) -> ApplicationError:
        field = exc.__cause__.__cause__.constraint_name
        match field:
            case "users_pkey":
                raise UserAlreadyExists()
