import pytest
import pytest_asyncio

from typing import Dict, Any, List
from datetime import datetime, timezone
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from faker import Faker

from src.application.translator.models.dto import TranslationHistoryDTO, TranslationRecordDTO
from src.adapters.database.models.translator.translation_history import translation_table
from src.adapters.database.repositories.translator.reader import HistoryReader

from tests.integrations.test_database.conftest import session

from .conftest import user_id


@pytest.fixture
def history_reader(session: AsyncSession) -> HistoryReader:
    return HistoryReader(session)


@pytest.fixture()
def history(user_id: int) -> List[Dict[str, Any]]:
    faker = Faker()
    return [
        {
            "user_id": user_id,
            "original_text": faker.text(),
            "translated_text": faker.text(),
            "datetime_of_translation": datetime.now(timezone.utc)
        }

        for _ in range(10)
    ]


@pytest_asyncio.fixture(autouse=True)
async def add_data(session: AsyncSession, history) -> None:
    for translate in history:
        stmt = insert(translation_table).values(
            translate
        )
        await session.execute(stmt)


@pytest.mark.asyncio
async def test_valid_get(history_reader: HistoryReader, history: List[Dict[str, Any]], user_id: int):
    res = await history_reader.get_translation_history(user_id)
    expected_history = TranslationHistoryDTO(
        [TranslationRecordDTO(row["original_text"],
                              row["translated_text"],
                              row["datetime_of_translation"])
         for row in history]
    )
    expected_history.messages.sort(key=lambda x: x.datetime_of_translation)
    assert res == expected_history
