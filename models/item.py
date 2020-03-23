"""This module contains the Item class"""

from settings import IMG_WIDTH
from .position import Position
from .factory import create_item_representation


class Item:
    """Represent a item on the map"""

    def __init__(self, map, image, name):
        self.map = map
        self.position = map.get_item_position()
        # use factory method for the representation of the item
        self.img = create_item_representation(image)
        self.name = name

    @property
    def img_position(self):
        """Return the computed image Position object"""
        x, y = self.position.position
        x *= IMG_WIDTH
        y *= IMG_WIDTH
        return Position(x, y)
