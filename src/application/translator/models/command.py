from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class TranslationMessage:
    text: str
    target_land: str = field(default='RU')
