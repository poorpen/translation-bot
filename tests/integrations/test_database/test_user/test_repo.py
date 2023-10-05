import random
import pytest

from typing import Dict, Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

from src.application.user.exceptions import UserAlreadyExists
from src.adapters.database.models.user.user import user_table
from src.adapters.database.repositories.user.repo import UserRepo

from tests.integrations.test_database.conftest import session


@pytest.fixture
def user_repo(session: AsyncSession) -> UserRepo:
    return UserRepo(session)


@pytest.fixture
def user_data(request) -> Dict[str, Any]:
    fake = Faker()
    user_data = {
        "telegram_id": random.randint(1000, 5000),
        "username": fake.first_name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name()
    }
    field_name = request.param
    if field_name:
        user_data[field_name] = None

    return user_data


@pytest.mark.asyncio
@pytest.mark.parametrize("user_data", [
    None,
    "username",
    "last_name"
], indirect=True)
async def test_valid_add_user(session: AsyncSession, user_repo: UserRepo, user_data: Dict[str, Any]):
    await user_repo.add_user(**user_data)
    stmt = select(user_table).where(user_table.c.telegram_id == user_data["telegram_id"])
    res = await session.execute(stmt)
    assert res.mappings().first() == user_data


@pytest.mark.asyncio
@pytest.mark.parametrize("user_data", [None], indirect=True)
async def test_invalid_add_user(user_repo: UserRepo, user_data: Dict[str, Any]):
    await user_repo.add_user(**user_data)
    with pytest.raises(UserAlreadyExists):
        await user_repo.add_user(**user_data)
