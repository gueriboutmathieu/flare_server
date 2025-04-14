class StreamNotFoundException(Exception):
    def __init__(self, message: str = "Stream not found") -> None:
        super().__init__(message)
