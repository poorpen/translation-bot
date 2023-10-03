from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.application.translator.models.command import TranslationMessage
from src.application.translator.models.dto import TranslationResultDTO
from src.application.translator.interfaces.translator import ITranslator
from src.application.translator.interfaces.db_gateway import IHistoryDBGateway
from src.application.translator.exceptions import EmptyMessage, MessageLimitExceeded


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

    async def __call__(self, command_data: TranslationMessage) -> TranslationResultDTO:
        user_info = self.identity_provider.get_access_policy()

        result = await self.translator.translate(text=command_data.text, target_land=command_data.target_land)

        try:
            await self.db_gateway.repo.add_translation(
                user_id=user_info.user_id,
                original_text=command_data.text,
                translated_text=result.text,
                datetime_of_translation=result.datetime_of_translation
            )
            await self.db_gateway.commit()
        except (EmptyMessage, MessageLimitExceeded):
            await self.db_gateway.rollback()

        return result
