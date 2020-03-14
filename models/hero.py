from pygame.image import load
from .position import Position

class Hero:
    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self.hero_img = load('images/' + 'MacGyver.png').convert()
        # hero_img = pygame.image.load(IMAGE_DIR + 'MacGyver.png').convert()

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
        x *= 30
        y *= 30
        return Position(x, y)
        # return x, y
        