from typing import Callable, ParamSpec, Coroutine, Any

from sqlalchemy.exc import SQLAlchemyError

from .exceptions import RepoError


def exception_mapper(func: Callable[[Any], Coroutine]):
    async def wrapped(*args: ParamSpec.args, **kwargs: ParamSpec.kwargs):
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError:
            raise RepoError()

    return wrapped
