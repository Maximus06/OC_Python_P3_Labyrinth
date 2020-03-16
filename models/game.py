import pygame
from sys import exit
from .map import Map
from .hero import Hero
from .item import Item
from settings import IMG_GARDIAN, IMG_WALL, IMG_WIDTH, IMG_NEEDLE, IMG_ETHER, IMG_TUBE

class Game:

    @classmethod
    def run(cls):        
        cls._init()

        cls.play = True
        while cls.play:
            #Limit the tick to 20 frames by secondes
            pygame.time.Clock().tick(20)
            cls._check_events()
            cls._update_screen()            
    
    @classmethod
    def _init(cls):        
        
        cls.screen = pygame.display.set_mode((450, 450))
        cls.map = Map('labyrinth.txt')
        cls.hero = Hero(cls.map)
        cls.items = []
        cls.create_items()
        
        pygame.display.set_caption("Mac Gyver Escape Game")
        
        cls._update_screen()

    @classmethod
    def _draw_wall(cls):
        #todo a déplacer dans la classe qui s'occupera du display
        
        gardian_img = pygame.image.load(IMG_GARDIAN).convert()
        wall_img = pygame.image.load(IMG_WALL).convert()

        for wall in cls.map._wall:
            x, y = wall.position            
            cls.screen.blit(wall_img, (y * IMG_WIDTH, x * IMG_WIDTH))

        # Gardian position
        x, y = cls.map.end.position
        cls.screen.blit(gardian_img, (y * IMG_WIDTH, x * IMG_WIDTH))               

    @classmethod
    def _check_events(cls):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.play = False
            elif event.type == pygame.KEYDOWN:
                cls._check_keydown_events(event)

    @classmethod
    def _check_keydown_events(cls, event):
        """Respond to keydown events"""        
        if event.key == pygame.K_RIGHT:
            cls.hero.move('right')
        elif event.key == pygame.K_LEFT:
            cls.hero.move('left')
        elif event.key == pygame.K_UP:
            cls.hero.move('up')
        elif event.key == pygame.K_DOWN:
            cls.hero.move('down')            
        elif event.key == pygame.K_F5:
            cls.reset()            
        # pygame map en querty donc event.key == pygame.K_q ne marche pas pour q
        elif event.unicode == 'q' or event.unicode == 'Q':            
            cls.play = False

    @classmethod
    def create_items(cls):
        """Create the 3 items on the maps"""
        needle = Item(cls.map, IMG_NEEDLE)
        cls.items.append(needle)
        ether = Item(cls.map, IMG_ETHER)
        cls.items.append(ether)        
        tube = Item(cls.map, IMG_TUBE)
        cls.items.append(tube)

    @classmethod
    def _update_screen(cls):
        """Update the screen."""
        # Background color
        cls.screen.fill((230, 230, 230))

        #Draw the labyrinth wall
        cls._draw_wall()

        # MacGyver image position
        x, y = cls.hero.img_position
        # print(f'update image to {x}, {y}')
        cls.screen.blit(cls.hero.hero_img , (y, x))
        
        # Display Items
        for item in cls.items:
            x, y = item.img_position        
            cls.screen.blit(item.img , (y, x))        

        pygame.display.flip()

    @classmethod
    def reset(cls):
        cls.hero = None
        cls.items.clear()
        cls.map = None
        cls.run()



