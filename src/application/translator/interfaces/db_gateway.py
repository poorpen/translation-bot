from src.common.applications.interfaces.db_gateway import IDBGateway

from .repo import IHistoryRepo
from .reader import IHistoryReader


class IHistoryDBGateway(IDBGateway):
    repo: IHistoryRepo
    reader: IHistoryReader
