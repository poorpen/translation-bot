from src.common.applications.interfaces.db_gateway import IDBGateway

from .repo import IHistoryRepo
from .reader import IHistoryReader


class IHistoryDBGateway(IDBGateway):
    history_repo: IHistoryRepo
    history_reader: IHistoryReader
