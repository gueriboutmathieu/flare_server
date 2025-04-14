from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from flare.routes.dtos.video_formats_dto import AudioFormatDto, VideoFormatDto


class VideoDto(BaseModel):
    id: str
    title: str
    channel_id: str
    channel_title: str
    thumbnail_url: str
    duration: int
    view_count: int
    upload_date: Optional[datetime]
    audio_formats: list[AudioFormatDto]
    video_formats: list[VideoFormatDto]
