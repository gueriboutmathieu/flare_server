from enum import Enum


class SearchType(str, Enum):
    VIDEO = "video"
    CHANNEL = "channel"
    PLAYLIST = "playlist"
    ALL = "all"
