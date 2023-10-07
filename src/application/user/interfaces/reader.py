from typing import Protocol


class IUserReader(Protocol):

    async def check_exist(self,telegram_id: int,) -> bool:
        raise NotImplemented
