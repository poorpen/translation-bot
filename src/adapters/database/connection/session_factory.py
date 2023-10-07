from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import DBConfig


def make_connection_string(config: DBConfig) -> str:
    return (
        f"{config.dbms}+{config.driver}://{config.user}:{config.password}@{config.host}:{config.port}/{config.db_name}"
    )


def session_factory(config: DBConfig) -> async_sessionmaker:
    engine = create_async_engine(
        make_connection_string(config)
    )
    return async_sessionmaker(engine)
