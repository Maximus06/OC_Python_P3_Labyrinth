from pygame.image import load
from .position import Position
from settings import IMG_WIDTH, IMG_HERO

class Hero:
    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        # self.hero_img = load(IMG_HERO).convert()
        

    def move(self, direction):
        # getattr permet d'appeler une méthode de l'objet position (up, down, left ou right)        
        method_position = getattr(self.position, direction)
        new_position = method_position()        
        if new_position in self.map:
            self.position = new_position        

    @property
    def img_position(self):
        """Return the computed Position of the hero image"""
        x, y = self.position.position
        x *= IMG_WIDTH
        y *= IMG_WIDTH
        return Position(x, y)
        # return x, y
        