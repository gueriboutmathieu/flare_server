from dataclasses import dataclass


@dataclass
class VideoFormat:
    id: str
    url: str
    codec: str
    height: int
    width: int
    fps: int
