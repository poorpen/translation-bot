from typing import Protocol

from src.application.translator.models.dto import TranslationHistoryDTO


class IHistoryReader(Protocol):

    async def get_translation_history(self, user_id: int) -> TranslationHistoryDTO:
        raise NotImplemented
