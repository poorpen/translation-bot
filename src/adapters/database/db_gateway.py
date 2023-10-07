from sqlalchemy.ext.asyncio import AsyncSession

from src.common.applications.interfaces.db_gateway import IDBGateway

from src.adapters.database.repositories.user import UserRepo, UserReader
from src.adapters.database.repositories.history import HistoryRepo, HistoryReader


class DBGateway(IDBGateway):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.history_repo = HistoryRepo(self._session)
        self.history_reader = HistoryReader(self._session)
        self.user_repo = UserRepo(self._session)
        self.user_reader = UserReader(self._session)

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
