from typing import Dict, Callable, Awaitable, Any, TypeVar, Type

Event = TypeVar("Event")
Handler = Callable[..., Awaitable[Any]]


class Director:

    def __init__(self):
        self._listeners: Dict[Type[Event], Handler] = {}

    def register_handler(self, event: Type[Event], handler: Handler) -> None:
        self._listeners[event] = handler

    async def execute(self, event: Event) -> Any:
        return await self._listeners[type(event)](event)
