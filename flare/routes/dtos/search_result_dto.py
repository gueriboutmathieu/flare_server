from flare.routes.dtos.video_dto import VideoDto
from flare.routes.dtos.playlist_dto import PlaylistDto
from flare.routes.dtos.channel_dto import ChannelDto

SearchResultDto = VideoDto | PlaylistDto | ChannelDto
