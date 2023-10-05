from sqlalchemy import Table, Column
from sqlalchemy.types import String, Integer

from src.common.adapters.database.models.base import metadata_obj

user_table = Table(
    "users",
    metadata_obj,
    Column("telegram_id", Integer, primary_key=True),
    Column("username", String),
    Column("first_name", String, nullable=False),
    Column("last_name", String)
)
