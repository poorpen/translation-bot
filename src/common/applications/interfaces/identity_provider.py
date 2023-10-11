from typing import Protocol

from src.common.applications.models.dto import UserInfoDTO


class IIdentityProvider(Protocol):

    def identify(self) -> UserInfoDTO:
        raise NotImplemented
