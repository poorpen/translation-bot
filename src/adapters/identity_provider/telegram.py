from aiogram.types import User

from src.common.applications.interfaces.identity_provider import IIdentityProvider

from src.common.applications.models.dto import UserInfoDTO


class TelegramIdentityProvider(IIdentityProvider):

    def __init__(self, user: User):
        self.user = user

    def identify(self) -> UserInfoDTO:
        return UserInfoDTO(self.user.id)
