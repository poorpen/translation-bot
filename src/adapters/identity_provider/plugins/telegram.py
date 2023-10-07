from aiogram.types import User

from src.common.adapters.identity_provider.plugins import BaseIdentifyPlugin
from src.common.applications.models.dto import UserInfoDTO


class TelegramIdentifyPlugin(BaseIdentifyPlugin[User]):

    def identify(self) -> UserInfoDTO:
        return UserInfoDTO(self.user_data.id)
