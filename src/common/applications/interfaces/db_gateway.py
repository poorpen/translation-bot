from typing import Protocol


class BaseDBGateway(Protocol):

    async def commit(self):
        raise NotImplemented

    async def rollback(self):
        raise NotImplemented
