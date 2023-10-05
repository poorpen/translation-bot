from sqlalchemy import select

from src.common.adapters.database.repositories.base import SQLAlchemyRepo
from src.common.adapters.database.exception_mapper import exception_mapper

from src.application.translator.models.dto import TranslationHistoryDTO
from src.application.translator.interfaces.reader import IHistoryReader
from src.adapters.database.models.translator.translation_history import translation_table

from .converters import to_dto


class HistoryReader(SQLAlchemyRepo, IHistoryReader):

    @exception_mapper
    async def get_translation_history(self, user_id: int) -> TranslationHistoryDTO:
        stmt = (
            select(
                translation_table.c.datetime_of_translation,
                translation_table.c.original_text,
                translation_table.c.translated_text
            )
            .where(
                translation_table.c.user_id == user_id
            )
        )

        result = await self._session.execute(stmt)
        mapped_result = result.mappings().all()

        return to_dto(mapped_result)
