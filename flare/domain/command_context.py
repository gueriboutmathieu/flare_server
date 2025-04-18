from typing import Protocol

from flare.repositories.user_repository import UserRepository
from flare.services.auth_service import AuthService
from flare.services.search_service import SearchService
from flare.services.streaming_service import StreamingService


class CommandContext(Protocol):
    @property
    def auth_service(self) -> AuthService:
        ...

    @property
    def search_service(self) -> SearchService:
        ...

    @property
    def streaming_service(self) -> StreamingService:
        ...

    @property
    def user_repository(self) -> UserRepository:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


def make_context(
    auth_service: AuthService,
    search_service: SearchService,
    streaming_service: StreamingService,
    user_repository: UserRepository,
) -> CommandContext:
    class CC:
        def __init__(self):
            self.auth_service = auth_service
            self.search_service = search_service
            self.streaming_service = streaming_service
            self.user_repository = user_repository

        def commit(self) -> None:
            ...

        def rollback(self) -> None:
            ...

    return CC()
