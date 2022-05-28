from enum import Enum, IntEnum


class Color(Enum):
    # TODO:
    red = ""
    blue = ""
    green = ""


class NoteContentPartType(IntEnum):
    text = 1
    image = 2
    todo = 3
