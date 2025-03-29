from typing import Protocol


class CommandContext(Protocol):
    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


def make_context() -> CommandContext:
    class CC:
        def commit(self) -> None:
            ...

        def rollback(self) -> None:
            ...

    return CC()
