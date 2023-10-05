from typing import Protocol
from datetime import datetime


class IHistoryRepo(Protocol):

    async def add_translation(
            self,
            user_id: int,
            original_text: str,
            translated_text: str,
            datetime_of_translation: datetime
    ) -> None:
        raise NotImplemented
