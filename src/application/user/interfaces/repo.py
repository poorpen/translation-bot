from typing import Protocol
from datetime import datetime


class IUserRepo(Protocol):

    async def add_user(
            self,
            telegram_id: int,
            username: str,
            first_name: str,
            last_name: str
    ) -> None:
        raise NotImplemented
