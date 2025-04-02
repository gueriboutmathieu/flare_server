from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from python_utils.entity import Entity


class Playlist(Entity):
    __tablename__ = "playlists"

    id: Mapped[str] = mapped_column(init=True, primary_key=True)
    title: Mapped[str] = mapped_column(init=True)
    url: Mapped[str] = mapped_column(init=True)
    channel_title: Mapped[str] = mapped_column(init=True)
    thumbnail_url: Mapped[str] = mapped_column(init=True)
    video_count: Mapped[int] = mapped_column(init=True)
    published_at: Mapped[datetime] = mapped_column(init=True)
    videos: Mapped[list["Video"]] = relationship(  # pyright: ignore  # noqa
        back_populates="playlist",
        init=False,
        default_factory=list,
    )

    channel_id: Mapped[Optional[str]] = mapped_column(ForeignKey("channels.id"), init=True)
    channel: Mapped[Optional["Channel"]] = relationship(back_populates="playlists", init=False)  # pyright: ignore  # noqa
