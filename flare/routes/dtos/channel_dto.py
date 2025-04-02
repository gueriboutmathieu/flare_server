from datetime import datetime
from pydantic import BaseModel


class ChannelDto(BaseModel):
    id: str
    title: str
    description: str
    url: str
    thumbnail_url: str
    video_count: int
    subscriber_count: int
    published_at: datetime
