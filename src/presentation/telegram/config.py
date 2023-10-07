import os

from dataclasses import dataclass

from src.adapters.translator import TranslatorConfig
from src.adapters.database.connection import DBConfig


@dataclass
class BotConfig:
    token: str


@dataclass
class Config:
    bot: BotConfig
    translator: TranslatorConfig
    db: DBConfig


def setup_config() -> Config:
    bot_config = BotConfig(token=os.environ["BOT_TOKEN"])
    translator = TranslatorConfig(auth_key=os.environ["AUTH_KEY"])
    db_config = DBConfig(
        dbms=os.environ["DBMS"],
        driver=os.environ["DRIVER"],
        db_name=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.getenv("DB_HOST", default="localhost"),
        port=os.getenv("DB_PORT", default=5432)
    )
    return Config(
        bot=bot_config,
        translator=translator,
        db=db_config
    )
