from typing import Protocol

from src.application.translator.models.dto import TranslatedMessageDTO


class ITranslator(Protocol):

    async def translate(self, text: str, target_lang: str) -> TranslatedMessageDTO:
        raise NotImplemented
