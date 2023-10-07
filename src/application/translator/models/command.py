from dataclasses import dataclass, field


@dataclass(frozen=True)
class TranslationMessage:
    text: str
    target_lang: str = field(default="RU")
    source_lang: str = field(default="EN")
