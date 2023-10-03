class EmptyMessage(Exception):

    def message(self) -> str:
        return "Вы отравили пустое сообщение."


class MessageLimitExceeded(Exception):

    def message(self) -> str:
        return "Длина отправленного вами сообщения превышает допустимое."
