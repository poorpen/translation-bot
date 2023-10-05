from src.common.applications.exceptions import UnexpectedError


class RepoError(UnexpectedError):

    def message(self) -> str:
        return ("Произошла непредвиденная ошибка при работе с базой данных. "
                "Пожалуйста воспользуйтесь нашим сервисом позже")
