from dataclasses import dataclass


class ApplicationError(Exception):

    def message(self) -> str:
        raise NotImplemented


class UnexpectedError(ApplicationError):

    def message(self) -> str:
        return "Произошла непредвиденная ошибка. Воспользуйтесь воспользуйтесь сервисом позже"
