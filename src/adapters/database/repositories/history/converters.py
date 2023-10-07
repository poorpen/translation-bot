from typing import Sequence

from sqlalchemy import RowMapping

from src.application.translator.models.dto import TranslationHistoryDTO, TranslationRecordDTO


def to_dto(data: Sequence[RowMapping]) -> TranslationHistoryDTO:
    history = TranslationHistoryDTO()
    for row in data:
        history.messages.append(
            TranslationRecordDTO(
                original_text=row["original_text"],
                translated_text=row["translated_text"],
                datetime_of_translation=row["datetime_of_translation"]
            )
        )
    history.messages.sort(key=lambda x: x.datetime_of_translation)
    return history
