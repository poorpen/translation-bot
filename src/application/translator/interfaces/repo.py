from typing import Protocol
from datetime import datetime

from src.application.translator.models.dto import TranslationResultDTO


class IHistoryRepo(Protocol):

    async def add_translation(
            self,
            user_id: int,
            original_text: str,
            translated_text: str,
            datetime_of_translation: datetime
    ) -> TranslationResultDTO:
        raise NotImplemented
