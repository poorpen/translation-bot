from aiohttp.client import ClientSession

from src.application.translator.interfaces.translator import ITranslator
from src.application.translator.models.dto import TranslatedMessageDTO
from src.application.translator.exceptions import MessageLimitExceeded

from .converters import to_result
from .exceptions import TooManyRequest, QuotaExceeded, TranslationError
from .config import TranslatorConfig


class DeepLTranslator(ITranslator):

    def __init__(self, config: TranslatorConfig):
        self._client = self._parametrize_client(config.auth_key, config.pro)

    async def translate(self, text: str, target_lang: str, source_lang: str) -> TranslatedMessageDTO:
        data = {"text": [text], "target_lang": target_lang, "source_lang": source_lang}
        async with self._client.post("/v2/translate", json=data) as resp:
            self._check_code(resp.status)
            resp_data = await resp.json()
            return to_result(resp_data)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):

        await self._client.close()

    @staticmethod
    def _parametrize_client(auth_key, pro) -> ClientSession:
        if pro:
            base_url = "https://api.deepl.com"
        else:
            base_url = "https://api-free.deepl.com"
        return ClientSession(base_url=base_url,
                             headers={
                                 "Authorization": "DeepL-Auth-Key " + auth_key,
                                 "Content-Type": "application/json"})

    @staticmethod
    def _check_code(code: int):
        match code:
            case 200 | 201 | 202:
                pass
            case 429:
                raise TooManyRequest()
            case 456:
                raise QuotaExceeded()
            case 413:
                raise MessageLimitExceeded()
            case _:
                raise TranslationError()
