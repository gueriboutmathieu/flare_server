from flare.domain.entities.channel_entity import Channel
from flare.domain.entities.playlist_entity import Playlist
from flare.domain.entities.video_entity import Video


SearchResult = Video | Channel | Playlist
