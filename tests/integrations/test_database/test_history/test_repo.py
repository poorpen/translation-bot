import pytest

from typing import Dict, Any
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.adapters.database.exceptions import RepoError
from src.adapters.database.models.translator.translation_history import translation_table
from src.adapters.database.repositories.translator.repo import HistoryRepo

from tests.integrations.test_database.conftest import session

from .conftest import user_id


@pytest.fixture
def history_repo(session: AsyncSession) -> HistoryRepo:
    yield HistoryRepo(session)


@pytest.fixture
def translated_message(user_id) -> Dict[str, Any]:
    return {
        "user_id": user_id,
        "original_text": "some text",
        "translated_text": "некоторый текст",
        "datetime_of_translation": datetime.now(timezone.utc)
    }


@pytest.fixture
def skipp_one_field(request, translated_message) -> Dict[str, Any]:
    field_name = request.param
    translated_message[field_name] = None
    return translated_message


@pytest.mark.asyncio
async def test_valid_add_translate(
        session: AsyncSession,
        history_repo: HistoryRepo,
        translated_message: Dict[str, Any],
        user_id: int,
):
    await history_repo.add_translation(**translated_message)
    stmt = select(translation_table.c.user_id,
                  translation_table.c.original_text,
                  translation_table.c.translated_text,
                  translation_table.c.datetime_of_translation
                  ).where(translation_table.c.user_id == user_id)
    res = await session.execute(stmt)
    assert res.mappings().first() == translated_message


@pytest.mark.asyncio
@pytest.mark.parametrize("skipp_one_field", [
    "user_id",
    "original_text",
    "translated_text",
    "datetime_of_translation"
], indirect=True)
async def test_invalid_add_translate(
        history_repo: HistoryRepo,
        skipp_one_field: Dict[str, Any]
):
    with pytest.raises(RepoError):
        await history_repo.add_translation(**skipp_one_field)
