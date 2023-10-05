from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import DateTime, String, Integer

from src.common.adapters.database.models.base import metadata_obj

translation_table = Table(
    "translation_history",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.telegram_id"), nullable=False),
    Column("original_text", String, nullable=False),
    Column("translated_text", String, nullable=False),
    Column("datetime_of_translation", DateTime(timezone=True), nullable=False)
)
