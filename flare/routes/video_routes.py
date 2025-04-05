from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from flare.domain.domain import Domain
from flare.domain.entities.user_entity import User
from flare.routes.utils.validate_user_wrapper import validate_user_wrapper


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.get("/videos/{video_id}/stream")
    async def stream_video(  # pyright: ignore[reportUnusedFunction]
        video_id: str,
        _: User = Depends(validate_user_wrapper(domain))
    ) -> StreamingResponse:
        subprocess = domain.stream(video_id)

        def generate():
            if subprocess.stdout is None:
                raise HTTPException(status_code=500, detail="Failed to stream video")
            try:
                while True:
                    chunk = subprocess.stdout.read(8192)
                    if not chunk:
                        break
                    yield chunk
            finally:
                subprocess.kill()

        return StreamingResponse(generate(), media_type="video/mp4", headers={"Accept-Ranges": "bytes"})
