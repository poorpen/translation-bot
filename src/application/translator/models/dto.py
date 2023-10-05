from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class TranslatedMessageDTO:
    text: str
    datetime_of_translation: datetime = field(default_factory=lambda: datetime.utcnow())


@dataclass
class TranslationRecordDTO:
    original_text: str
    translated_text: str
    datetime_of_translation: datetime


@dataclass(frozen=True)
class TranslationHistoryDTO:
    messages: List[TranslationRecordDTO] = field(default_factory=list)
