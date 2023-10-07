from src.common.applications.interfaces.db_gateway import IDBGateway

from .repo import IUserRepo
from .reader import IUserReader


class IUserDBGateway(IDBGateway):
    user_repo: IUserRepo
    user_reader: IUserReader
