from typing import TypeVar, Generic

from src.common.applications.models.dto import UserInfoDTO

T = TypeVar("T")


class BaseIdentifyPlugin(Generic[T]):

    def __init__(self, user_data: T):
        self.user_data = user_data

    def identify(self) -> UserInfoDTO:
        raise NotImplemented
