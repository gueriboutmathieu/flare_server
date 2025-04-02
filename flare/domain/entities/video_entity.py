from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from python_utils.entity import Entity


class Video(Entity):
    __tablename__ = "videos"

    id: Mapped[str] = mapped_column(init=True, primary_key=True)
    title: Mapped[str] = mapped_column(init=True)
    url: Mapped[str] = mapped_column(init=True)
    channel_title: Mapped[str] = mapped_column(init=True)
    thumbnail_url: Mapped[str] = mapped_column(init=True)
    duration: Mapped[int] = mapped_column(init=True)
    view_count: Mapped[int] = mapped_column(init=True)
    published_at: Mapped[datetime] = mapped_column(init=True)

    playlist_id: Mapped[Optional[str]] = mapped_column(ForeignKey("playlists.id"), init=True)
    playlist: Mapped[Optional["Playlist"]] = relationship(back_populates="videos", init=False)  # pyright: ignore  # noqa

    channel_id: Mapped[Optional[str]] = mapped_column(ForeignKey("channels.id"), init=True)
    channel: Mapped[Optional["Channel"]] = relationship(back_populates="videos", init=False)  # pyright: ignore  # noqa
