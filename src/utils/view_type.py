from enum import Enum, auto


class ViewType(Enum):
    MENU = auto()
    CHATS = auto()
    CALLS = auto()
    AI = auto()
    STARRED_MESSAGES = auto()
    ARCHIVE = auto()
    SETTINGS = auto()
    PROFILE = auto()
    STATUS = auto()
