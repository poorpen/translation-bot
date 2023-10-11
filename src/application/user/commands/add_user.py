from src.common.applications.exceptions import ApplicationError

from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.application.user.models.command import AddUser
from src.application.user.interfaces.db_gateway import IUserDBGateway


class AddUserCommand:

    def __init__(
            self,
            db_gateway: IUserDBGateway,
            identity_provider: IIdentityProvider
    ):
        self.db_gateway = db_gateway
        self.identity_provider = identity_provider

    async def __call__(self, command_data: AddUser) -> None:
        user_info = self.identity_provider.identify()

        try:
            await self.db_gateway.user_repo.add_user(
                telegram_id=user_info.user_id,
                username=command_data.username,
                first_name=command_data.first_name,
                last_name=command_data.last_name

            )
            await self.db_gateway.commit()
        except ApplicationError as exc:
            await self.db_gateway.rollback()
            raise exc
