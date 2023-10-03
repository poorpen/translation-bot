from typing import Protocol

from src.common.applications.models.dto import AccessDTO


class IIdentityProvider(Protocol):

    def get_access_policy(self) -> AccessDTO:
        raise NotImplemented
