from pydantic import BaseModel


class AudioFormatDto(BaseModel):
    id: str
    url: str
    codec: str
    abr: float


class VideoFormatDto(BaseModel):
    id: str
    url: str
    codec: str
    height: int
    width: int
    fps: int
