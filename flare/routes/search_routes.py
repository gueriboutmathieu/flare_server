from fastapi import Depends, FastAPI

from flare.domain.domain import Domain
from flare.domain.entities.channel_entity import Channel
from flare.domain.entities.playlist_entity import Playlist
from flare.domain.entities.search_type import SearchType
from flare.domain.entities.user_entity import User
from flare.domain.entities.video_entity import Video
from flare.routes.dtos.channel_dto import ChannelDto
from flare.routes.dtos.playlist_dto import PlaylistDto
from flare.routes.dtos.search_result_dto import SearchResultDto
from flare.routes.dtos.video_dto import VideoDto
from flare.routes.utils.validate_user_wrapper import validate_user_wrapper


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/search")
    async def search(  # pyright: ignore[reportUnusedFunction]
        query: str,
        search_type: SearchType = SearchType.ALL,
        _: User = Depends(validate_user_wrapper(domain))
    ) -> list[SearchResultDto]:
        search_results = domain.search(query, search_type)

        search_result_dtos: list[SearchResultDto] = []
        for search_result in search_results:
            match search_result:
                case Video():
                    search_result_dtos.append(VideoDto(**search_result.__dict__))
                case Playlist():
                    search_result_dtos.append(PlaylistDto(**search_result.__dict__))
                case Channel():
                    search_result_dtos.append(ChannelDto(**search_result.__dict__))
        return search_result_dtos
