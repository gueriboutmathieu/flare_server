from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from python_utils.entity import Entity


class Channel(Entity):
    __tablename__ = "channels"

    id: Mapped[str] = mapped_column(init=True, primary_key=True)
    title: Mapped[str] = mapped_column(init=True)
    description: Mapped[str] = mapped_column(init=True)
    url: Mapped[str] = mapped_column(init=True)
    thumbnail_url: Mapped[str] = mapped_column(init=True)
    video_count: Mapped[int] = mapped_column(init=True)
    subscriber_count: Mapped[int] = mapped_column(init=True)
    published_at: Mapped[datetime] = mapped_column(init=True)
    videos: Mapped[list["Video"]] = relationship(  # pyright: ignore  # noqa
        back_populates="channel",
        init=False,
        default_factory=list,
    )
    playlists: Mapped[list["Playlist"]] = relationship(  # pyright: ignore  # noqa
        back_populates="channel",
        init=False,
        default_factory=list,
    )
