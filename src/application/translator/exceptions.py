from src.common.applications.exceptions import ApplicationError


class MessageLimitExceeded(ApplicationError):

    def message(self) -> str:
        return "Длина отправленного вами сообщения превышает допустимое."
