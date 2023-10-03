from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class TranslationMessage:
    text: str
    datetime_of_translation: datetime = field(default_factory=datetime.utcnow)
