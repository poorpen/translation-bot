import os
import asyncio
import pathlib
import pytest
import pytest_asyncio

from typing import AsyncGenerator, Generator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from alembic.config import Config
from alembic.command import upgrade
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def postgres_url():
    with PostgresContainer("postgres:15") as postgres:
        postgres_url_ = postgres.get_connection_url()
        yield postgres_url_.replace("psycopg2", "asyncpg")


@pytest.fixture(scope='session')
def alembic_config(postgres_url):
    current_path = pathlib.Path(os.getcwd())
    path = filter(lambda x: x.name == "translation-bot", list(current_path.parents) + [current_path])
    os.chdir(*path)
    alembic_config = Config("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", postgres_url)
    return alembic_config


@pytest.fixture(scope="session", autouse=True)
def upgrade_schema_db(alembic_config: Config) -> None:
    upgrade(alembic_config, "head")


@pytest_asyncio.fixture(scope="session")
async def session_factory(postgres_url: str):
    engine = create_async_engine(url=postgres_url)
    yield async_sessionmaker(bind=engine)
    await engine.dispose()


@pytest_asyncio.fixture
async def session(session_factory: async_sessionmaker) -> AsyncGenerator:
    async with session_factory() as session_:
        yield session_
        await session_.rollback()
