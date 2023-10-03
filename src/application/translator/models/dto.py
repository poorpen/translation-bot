from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class TranslationResult:
    text: str
    datetime_of_translation: datetime


@dataclass(frozen=True)
class TranslationHistory:
    messages: List[TranslationResult]

