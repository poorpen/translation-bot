from dataclasses import dataclass


@dataclass(frozen=True)
class UserInfoDTO:
    user_id: int

