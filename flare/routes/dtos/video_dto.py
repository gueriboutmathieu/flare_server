from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class VideoDto(BaseModel):
    id: str
    title: str
    url: str
    channel_title: str
    thumbnail_url: str
    duration: int
    view_count: int
    published_at: datetime
    playlist_id: Optional[str] = None
    channel_id: Optional[str] = None
