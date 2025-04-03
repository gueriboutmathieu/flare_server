from pydantic import BaseModel
from uuid import UUID


class UserDto(BaseModel):
    id: UUID
    name: str
