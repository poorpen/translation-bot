from src.application.translator.models.dto import TranslatedMessageDTO


def to_result(data: dict) -> TranslatedMessageDTO:
    text = data["translations"][0]["text"]
    return TranslatedMessageDTO(text=text)
