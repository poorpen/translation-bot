from src.common.applications.exceptions import UnexpectedError


class TranslationError(UnexpectedError):

    def message(self) -> str:
        return ("Произошла непредвиденная ошибка при работе с поставщиком."
                "Пожалуйста воспользуйтесь нашим сервисом позже")


class TooManyRequest(TranslationError):

    def message(self) -> str:
        return "Большое количество запросов. Подождите и отвеправьте ваше сообщение позже"


class QuotaExceeded(TranslationError):

    def message(self) -> str:
        return "Превышен лимит общимх символов. Подождите пока мы решаем эту проблему"
