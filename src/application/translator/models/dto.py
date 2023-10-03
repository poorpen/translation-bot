from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List


@dataclass(frozen=True)
class TranslationResultDTO:
    text: str
    datetime_of_translation: datetime = field(default_factory=datetime.utcnow)


@dataclass(frozen=True)
class TranslationHistoryDTO:
    messages: List[TranslationResultDTO]
