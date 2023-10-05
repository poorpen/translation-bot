from typing import Protocol

from src.common.applications.models.dto import UserInfoDTO


class IIdentityProvider(Protocol):

    def get_identification_data(self) -> UserInfoDTO:
        raise NotImplemented
