from typing import Protocol

from flare.services.search_service import SearchService


class CommandContext(Protocol):
    @property
    def search_service(self) -> SearchService:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


def make_context(search_service: SearchService) -> CommandContext:
    class CC:
        def __init__(self):
            self.search_service = search_service

        def commit(self) -> None:
            ...

        def rollback(self) -> None:
            ...

    return CC()
