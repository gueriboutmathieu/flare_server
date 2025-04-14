from dataclasses import dataclass


@dataclass
class AudioFormat:
    id: str
    url: str
    codec: str
    abr: float
