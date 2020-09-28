from enum import Enum, unique, auto


@unique
class LibraryEnums(Enum):
    CHECKED_IN = auto()
    CHECKED_OUT = auto()
    BOOK = auto()
    CD = auto()
    MAGAZINE = auto()
    DVD = auto()
    UNKNOWN = auto()