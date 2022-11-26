"""Constante"""
from enum import IntEnum


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

class Url():
    """Urls"""
    BASE = "https://www.rika-firenet.com"
    LOGIN = "/web/login"
    STOVE = "/web/stove/"
    API = "/api/client/"
