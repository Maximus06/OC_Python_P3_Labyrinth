import pygame
from settings import IMG_HERO, IMG_GARDIAN, IMG_WALL, IMG_WIDTH, IMG_NEEDLE, IMG_ETHER, IMG_TUBE
from settings import IMG_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH

class View:
    """The class view is responsible for render graphism"""

    def __init__(self, map):
        self.map = map
        self.hero_img = pygame.image.load(IMG_HERO).convert()
        self.wall_img = pygame.image.load(IMG_WALL).convert()
        self.guardian_img = pygame.image.load(IMG_GARDIAN).convert()        
        pygame.display.set_caption("Mac Gyver Escape Game")
    
    @classmethod
    def set_video_mode(cls):
        cls.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def render(self):        
        #background color
        View.screen.fill((230, 230, 230))

        # Draw the wall
        for wall in self.map._wall:
            x, y = wall.position            
            View.screen.blit(self.wall_img, (y * IMG_WIDTH, x * IMG_WIDTH))
        
        # Draw the hero
        x, y = self.map.hero.img_position
        View.screen.blit(self.hero_img, (y, x))
        
        # Draw the guardian
        x, y = self.map.end
        View.screen.blit(self.guardian_img, (y * IMG_WIDTH, x * IMG_WIDTH))

        # Draw the Items
        for item in self.map.items:
            x, y = item.img_position        
            View.screen.blit(item.img , (y, x))

        # Refresh
        pygame.display.flip()
        
