from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from typing import cast, IO

from flare.domain.domain import Domain
from flare.domain.entities.user_entity import User
from flare.domain.exceptions.stream_exceptions import StreamNotFoundException
from flare.routes.dtos.video_dto import VideoDto
from flare.routes.dtos.video_formats_dto import AudioFormatDto, VideoFormatDto
from flare.routes.utils.validate_user_wrapper import validate_user_wrapper


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/videos/search")
    async def search(  # pyright: ignore[reportUnusedFunction]
        query: str,
        _: User = Depends(validate_user_wrapper(domain))
    ) -> list[VideoDto]:
        videos = domain.search(query)

        video_dtos: list[VideoDto] = []
        for video in videos:
                video_dtos.append(
                    VideoDto(
                        id=video.id,
                        title=video.title,
                        channel_id=video.channel_id,
                        channel_title=video.channel_title,
                        thumbnail_url=video.thumbnail_url,
                        duration=video.duration,
                        view_count=video.view_count,
                        upload_date=video.upload_date,
                        audio_formats=[],
                        video_formats=[],
                    )
                )

        return video_dtos

    @fastapi_app.get("/videos/{video_id}/with-formats")
    async def get_formats(  # pyright: ignore[reportUnusedFunction]
        video_id: str,
        # _: User = Depends(validate_user_wrapper(domain))
    ) -> VideoDto:
        video = domain.get_video_with_formats(video_id)

        audio_format_dtos = [
            AudioFormatDto(
                id=audio_format.id,
                url=audio_format.url,
                codec=audio_format.codec,
                abr=audio_format.abr,
            )
            for audio_format in video.audio_formats
        ]
        video_format_dtos = [
            VideoFormatDto(
                id=video_format.id,
                url=video_format.url,
                codec=video_format.codec,
                height=video_format.height,
                width=video_format.width,
                fps=video_format.fps,
            )
            for video_format in video.video_formats
        ]
        return VideoDto(
            id=video.id,
            title=video.title,
            channel_id=video.channel_id,
            channel_title=video.channel_title,
            thumbnail_url=video.thumbnail_url,
            duration=video.duration,
            view_count=video.view_count,
            upload_date=video.upload_date,
            audio_formats=audio_format_dtos,
            video_formats=video_format_dtos,
        )

    @fastapi_app.get("/videos/{video_id}/stream")
    async def stream(  # pyright: ignore[reportUnusedFunction]
        access_token: str,
        video_id: str,
        start_at: int,
        container: str,
        audio_url: str,
        video_url: str,
    ) -> StreamingResponse:
        domain.validate_user(access_token)

        subprocess = domain.stream(video_id, start_at, audio_url, video_url, container)

        return StreamingResponse(cast(IO[bytes], subprocess.stdout), media_type=f"video/{container}")

    @fastapi_app.post("/videos/{video_id}/end-stream")
    async def end_stream(  # pyright: ignore[reportUnusedFunction]
        video_id: str,
        _: User = Depends(validate_user_wrapper(domain))
    ) -> None:
        try:
            domain.end_stream(video_id)
        except StreamNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e)) from e
