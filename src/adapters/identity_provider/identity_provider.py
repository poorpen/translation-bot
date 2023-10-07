from typing import Any, Type

from src.common.applications.interfaces.identity_provider import IIdentityProvider
from src.common.applications.models.dto import UserInfoDTO
from src.common.adapters.identity_provider.plugins import BaseIdentifyPlugin


class IdentityProvider(IIdentityProvider):

    def __init__(
            self,
            plugin: Type[BaseIdentifyPlugin],
            user_data: Any
    ):
        self._plugin = plugin(user_data)

    def get_identification_data(self) -> UserInfoDTO:
        return self._plugin.identify()
