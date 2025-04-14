from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from flare.domain.entities.audio_format import AudioFormat
from flare.domain.entities.video_format import VideoFormat


@dataclass
class Video:
    id: str
    title: str
    thumbnail_url: str
    channel_id: str
    channel_title: str
    duration: int
    view_count: int
    upload_date: Optional[datetime]
    audio_formats: list[AudioFormat]
    video_formats: list[VideoFormat]
