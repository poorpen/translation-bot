from typing import Protocol


class IDBGateway(Protocol):

    async def commit(self):
        raise NotImplemented

    async def rollback(self):
        raise NotImplemented
