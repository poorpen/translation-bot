from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.application.translator.models.dto import TranslationHistoryDTO
from src.application.translator.interfaces.db_gateway import IHistoryDBGateway


class GetHistoryQuery:

    def __init__(
            self,
            db_gateway: IHistoryDBGateway,
            identity_provider: IIdentityProvider
    ):
        self.db_gateway = db_gateway
        self.identity_provider = identity_provider

    async def __call__(self) -> TranslationHistoryDTO:
        user_info = self.identity_provider.get_identification_data()

        return await self.db_gateway.history_reader.get_translation_history(user_info.user_id)
