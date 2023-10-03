from dataclasses import dataclass


@dataclass(frozen=True)
class AccessDTO:
    user_id: int
