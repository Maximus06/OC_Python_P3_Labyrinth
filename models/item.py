"""This module contains the Item class"""

from settings import IMG_WIDTH
from .position import Position
from .factory import create_item_representation


class Item:
    """Represent a item on the map"""

    def __init__(self, map, image, name):
        self._map = map
        self._position = self._map.get_random_position()
        # use factory method for the representation of the item
        self._img = create_item_representation(image)
        self._name = name

    @property
    def image(self):
        """Return the item image."""
        return self._img

    @property
    def position(self):
        """Return the Position object of the item."""
        return self._position

    @property
    def img_position(self):
        """Return the computed image Position object"""
        x, y = self._position.position
        x *= IMG_WIDTH
        y *= IMG_WIDTH
        return Position(x, y)

    @property
    def name(self):
        """Return String of the name"""
        return self._name

    @name.setter
    def name(self, value):
        """Set the String of the name"""
        self._name = value
