from pygame.image import load
from .position import Position
from settings import IMG_WIDTH

class Item:
    def __init__(self, map, image):
        self.map = map
        self.position = map.get_item_position()
        self.img = load(image).convert()        
    
    def __repr__(self):
        return f'My image is {self.img} to position {self.position}'

    @property
    def img_position(self):
        """Return the computed Position of image"""
        x, y = self.position.position
        x *= IMG_WIDTH
        y *= IMG_WIDTH
        return Position(x, y)
        
        