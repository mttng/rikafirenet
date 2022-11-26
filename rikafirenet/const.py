"""Constante"""
from enum import IntEnum, Enum
import string


class OperatingMode(IntEnum):
    """Operating mode"""
    MANUAL = 0
    AUTO = 1
    CONFORT = 2
    DEFROST = 4

class State(IntEnum):
    """Operating mode"""
    MANUAL = 0
    AUTO = 1
    CONFORT = 2
    DEFROST = 4

class Url(Enum):
    """Urls"""
    BASE = "https://www.rika-firenet.com"
    LOGIN = "/web/login"
    STOVE = "/web/stove/"
    API = "/api/client/"
