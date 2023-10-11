from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.application.user.interfaces.db_gateway import IUserDBGateway


class CheckExistQuery:

    def __init__(
            self,
            db_gateway: IUserDBGateway,
            identity_provider: IIdentityProvider
    ):
        self.db_gateway = db_gateway
        self.identity_provider = identity_provider

    async def __call__(self, *args, **kwargs) -> bool:
        user_info = self.identity_provider.identify()

        return await self.db_gateway.user_reader.check_exist(user_info.user_id)
