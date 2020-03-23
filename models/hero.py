"""This module contains the Hero class"""


from .position import Position
from settings import IMG_WIDTH


class Hero:
    """This class represents MacGyver"""

    def __init__(self, map):
        """Init the class attributs"""
        self.map = map
        self.position = self.map.start
        self._items = set()

    @property
    def items(self):
        """Return the Items set of the hero"""
        return self._items

    @items.setter
    def items(self, value):
        """Add a item to the items set.
        Args:
            value:
        """
        self._items.add(value)

    @property
    def item_number(self):
        """Return the len of the items set"""
        return len(self._items)

    @property
    def img_position(self):
        """Return the computed Position of the hero image"""
        x, y = self.position.position
        x *= IMG_WIDTH
        y *= IMG_WIDTH
        return Position(x, y)

    def move(self, direction):
        """Update the Hero position.
        Args:
            direction: String of the direction (up, down, left, right).
        """
        # TODO : make direction a enum
        # get the method from position object
        method_position = getattr(self.position, direction)
        new_position = method_position()
        if new_position in self.map:
            self.position = new_position
