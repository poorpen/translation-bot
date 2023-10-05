from src.common.applications.exceptions import ApplicationError


class UserAlreadyExists(ApplicationError):

    def message(self) -> str:
        pass
