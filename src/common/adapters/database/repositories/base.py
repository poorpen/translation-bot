from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyRepo:

    def __init__(self, session: AsyncSession):
        self._session = session
