from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.application.translator.models.query import GetHistory
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

    async def __call__(self, query_data: GetHistory) -> TranslationHistoryDTO:
        user_id = query_data.user_id

        if not user_id:
            user_id = self.identity_provider.get_access_policy()

        return await self.db_gateway.reader.get_translation_history(user_id)
