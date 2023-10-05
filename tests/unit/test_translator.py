import datetime
import random

import pytest
import pytest_asyncio

from typing import Callable, Coroutine, Type
from unittest import mock
from aiohttp import web
from aiohttp.test_utils import TestClient

from src.common.applications.exceptions import ApplicationError

from src.application.translator.models.dto import TranslatedMessageDTO
from src.application.translator.exceptions import MessageLimitExceeded
from src.adapters.translator.translator import DeepLTranslator
from src.adapters.translator.exceptions import TooManyRequest, QuotaExceeded, TranslationError


@pytest.fixture
def translated_text() -> str:
    return "поддельный перевод текста"


@pytest.fixture
def translation_result(translated_text):
    async def handler(request):
        body = await request.json()
        text = body["text"][0]
        if text.isdigit():
            response = web.Response(status=int(text))
        else:
            response = web.json_response(data={
                "translations": [
                    {
                        "detected_source_language": "EN",
                        "text": translated_text
                    }
                ]
            }, status=random.choice([200, 201, 202]))

        return response

    return handler


@pytest_asyncio.fixture
async def fake_client(aiohttp_client: Callable, translation_result: Callable[[...], Coroutine]):
    app = web.Application()
    app.router.add_post('/v2/translate', translation_result)
    return await aiohttp_client(app)


@pytest_asyncio.fixture
async def translator(fake_client: TestClient) -> DeepLTranslator:
    with mock.patch('src.adapters.translator.translator.ClientSession') as mock_client:
        mock_client.return_value = fake_client
        deepl = DeepLTranslator("key")
        async with deepl as d:
            yield d


@pytest.mark.asyncio
async def test_valid_translate(translator: DeepLTranslator, translated_text: str):
    frozen_datetime = datetime.datetime(2023, 1, 1)
    with mock.patch("src.application.translator.models.dto.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = frozen_datetime
        res = await translator.translate('some_text', 'ru')
        assert res == TranslatedMessageDTO(translated_text, frozen_datetime)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "code, exc", [
        ("429", TooManyRequest),
        ("456", QuotaExceeded),
        ("413", MessageLimitExceeded),
        ("500", TranslationError)
    ]
)
async def test_invalid_translate(translator: DeepLTranslator, code: str, exc: Type[ApplicationError]):
    with pytest.raises(exc):
        await translator.translate(code, target_lang="RU")
