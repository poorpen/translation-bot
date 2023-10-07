from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.common.applications.exceptions import ApplicationError

from src.application.translator.models.command import TranslationMessage
from src.application.translator.models.dto import TranslatedMessageDTO
from src.application.translator.interfaces.translator import ITranslator
from src.application.translator.interfaces.db_gateway import IHistoryDBGateway


class TranslateMessageCommand:

    def __init__(
            self,
            translator: ITranslator,
            db_gateway: IHistoryDBGateway,
            identity_provider: IIdentityProvider
    ):
        self.translator = translator
        self.db_gateway = db_gateway
        self.identity_provider = identity_provider

    async def __call__(self, command_data: TranslationMessage) -> TranslatedMessageDTO:
        user_info = self.identity_provider.get_identification_data()

        result = await self.translator.translate(
            text=command_data.text,
            target_lang=command_data.target_lang,
            source_lang=command_data.source_lang
        )

        try:
            await self.db_gateway.history_repo.add_translation(
                user_id=user_info.user_id,
                original_text=command_data.text,
                translated_text=result.text,
                datetime_of_translation=result.datetime_of_translation
            )
            await self.db_gateway.commit()
        except ApplicationError as exc:
            await self.db_gateway.rollback()
            raise exc

        return result
