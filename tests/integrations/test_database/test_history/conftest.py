import pytest
import pytest_asyncio

from typing import AsyncGenerator

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.adapters.database.models.user.user import user_table

from tests.integrations.test_database.conftest import session_factory


@pytest.fixture(scope="session")
def user_id() -> int:
    return 1234


@pytest_asyncio.fixture(scope="session", autouse=True)
async def data_preparation(session_factory: async_sessionmaker, user_id: int) -> None:
    async with session_factory() as session:
        stmt = insert(user_table).values(
            telegram_id=user_id,
            first_name="bomboclaut"
        )
        await session.execute(stmt)
        await session.commit()
