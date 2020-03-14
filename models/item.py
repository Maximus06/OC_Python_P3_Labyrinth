from pygame.image import load
from .position import Position

class Item:
    def __init__(self, map, image):
        self.map = map
        self.position = map.get_item_position()
        self.img = load('images/' + image).convert()
        # hero_img = pygame.image.load(IMAGE_DIR + 'MacGyver.png').convert()
    
    def __repr__(self):
        return f'My image is {self.img} to position {self.position}'

    @property
    def img_position(self):
        """Return the computed Position of image"""
        x, y = self.position.position
        x *= 30
        y *= 30
        return Position(x, y)
        
        