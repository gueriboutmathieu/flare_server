from datetime import datetime
from pydantic import BaseModel


class PlaylistDto(BaseModel):
    id: str
    title: str
    url: str
    channel_id: str
    channel_title: str
    thumbnail_url: str
    video_count: int
    published_at: datetime
