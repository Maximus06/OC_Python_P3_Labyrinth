import pygame
from sys import exit
from .map import Map
from .hero import Hero
from .item import Item
from settings import IMG_GARDIAN, IMG_WALL, IMG_WIDTH, IMG_NEEDLE, IMG_ETHER, IMG_TUBE, TICK
from .views import View

class Game:
    """The Game class manages the game flow"""

    @classmethod
    def run(cls):        
        cls._init()

        cls.play = True
        while cls.play:
            #Limit the tick to x frames by secondes
            pygame.time.Clock().tick(TICK)
            cls._check_events()
            cls.view.render()        
    
    @classmethod
    def _init(cls):        
        # the video mode must be set before loading images(in map).
        View.set_video_mode()
        cls.map = Map('labyrinth.txt')        
        cls.view = View(cls.map)        

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
            cls.map.hero.move('right')
        elif event.key == pygame.K_LEFT:
            cls.map.hero.move('left')
        elif event.key == pygame.K_UP:
            cls.map.hero.move('up')
        elif event.key == pygame.K_DOWN:
            cls.map.hero.move('down')            
        elif event.key == pygame.K_F5:
            cls.reset()            
        # Use unicode here cause pygame map in querty mode
        elif event.unicode == 'q' or event.unicode == 'Q':            
            cls.play = False        

    @classmethod
    def reset(cls):
        """This method reset the game"""        
        # cls.map = None
        del cls.map
        cls.run()



