from typing import Callable, ParamSpec, Coroutine, Any

from sqlalchemy.exc import SQLAlchemyError

from .exceptions import RepoError

Param = ParamSpec("Param")


def exception_mapper(func: Callable[..., Coroutine]):
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs):
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError:
            raise RepoError()

    return wrapped
