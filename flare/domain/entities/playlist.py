from dataclasses import dataclass
from datetime import datetime

from flare.domain.entities.video_entity import Video


@dataclass
class Playlist:
    id: str
    title: str
    channel_id: str
    channel_title: str
    thumbnail_url: str
    video_count: int
    view_count: int
    modified_date: datetime
    videos: list[Video]
