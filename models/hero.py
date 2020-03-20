from pygame.image import load
from .position import Position
from settings import IMG_WIDTH, IMG_HERO

class Hero:
    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self._items = set()

    @property
    def items(self):
        return self._items
    @items.setter       
    def items(self, value):
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
        # getattr permet d'appeler une méthode de l'objet position (up, down, left ou right)        
        method_position = getattr(self.position, direction)
        new_position = method_position()        
        if new_position in self.map:
            self.position = new_position        

        