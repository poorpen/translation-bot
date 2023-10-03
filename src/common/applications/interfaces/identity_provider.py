from typing import Protocol

from src.common.applications.models.dto import UserInfoDTO


class IIdentityProvider(Protocol):

    def get_access_policy(self) -> UserInfoDTO:
        raise NotImplemented
