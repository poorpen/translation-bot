from dataclasses import dataclass


@dataclass
class TranslatorConfig:
    auth_key: str
    pro: bool = False
