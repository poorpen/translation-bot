from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class TranslationMessage:
    text: str
    target_lang: str = field(default='RU')
