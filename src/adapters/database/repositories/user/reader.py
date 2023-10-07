from sqlalchemy import select

from src.common.adapters.database.repositories.base import SQLAlchemyRepo
from src.common.adapters.database.exception_mapper import exception_mapper

from src.application.user.interfaces.reader import IUserReader
from src.adapters.database.models.user.user import user_table


class UserReader(SQLAlchemyRepo, IUserReader):

    @exception_mapper
    async def check_exist(self, telegram_id: int, ) -> bool:
        stmt = select(user_table.c.telegram_id).where(user_table.c.telegram_id == telegram_id)
        result = await self._session.execute(stmt)
        user_id = result.scalar()
        if user_id:
            return True
        return False
