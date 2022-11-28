"""Main module."""
# from .client import FirenetClient
from .sensors import StoveSensors
from .controls import StoveControls
# from .coordinator import StoveCoordinator

class Stove(StoveSensors, StoveControls):
    """Class representing a stove"""
