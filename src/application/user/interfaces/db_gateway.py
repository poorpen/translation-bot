from src.common.applications.interfaces.db_gateway import IDBGateway

from .repo import IUserRepo


class IUserDBGateWay(IDBGateway):
    user_repo: IUserRepo
