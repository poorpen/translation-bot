from datetime import datetime

from sqlalchemy import insert

from src.common.adapters.database.repositories.base import SQLAlchemyRepo
from src.common.adapters.database.exception_mapper import exception_mapper

from src.application.translator.interfaces.repo import IHistoryRepo
from src.adapters.database.models.translator.translation_history import translation_table


class HistoryRepo(SQLAlchemyRepo, IHistoryRepo):

    @exception_mapper
    async def add_translation(
            self,
            user_id: int,
            original_text: str,
            translated_text: str,
            datetime_of_translation: datetime
    ) -> None:
        stmt = insert(translation_table).values(
            user_id=user_id,
            original_text=original_text,
            translated_text=translated_text,
            datetime_of_translation=datetime_of_translation
        )
        await self._session.execute(stmt)
