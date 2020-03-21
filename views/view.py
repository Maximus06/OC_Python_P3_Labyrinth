"""This module contains the View class"""

import pygame
from pygame.locals import color as pg_color

from settings import (IMG_HERO, IMG_GARDIAN, IMG_WALL, IMG_WIDTH, IMG_NEEDLE,
                     IMG_ETHER, IMG_TUBE, IMG_WIDTH, SCREEN_HEIGHT,
                     SCREEN_WIDTH, BG_COLOR, HELP_MSG, INIT_MSG)

class View:
    """This class is responsible for render graphism using pygame librairy"""

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self, map):
        """initialize the class attributs.
        Args:
            map: a Map object representing the labyrinth.
        """
        self.map = map
        self.hero_img = pygame.image.load(IMG_HERO).convert()
        self.wall_img = pygame.image.load(IMG_WALL).convert()
        # Set transparency for white color
        self.hero_img.set_colorkey((255,255,255)) 
        self.wall_img.set_colorkey((255,255,255)) 
        self.guardian_img = pygame.image.load(IMG_GARDIAN).convert()        
        pygame.display.set_caption("Mac Gyver Escape Game")

        self.font_help = pygame.font.SysFont("arial", 16, bold=True)        
        self.font_text = pygame.font.SysFont("arial", 18, bold=True)        
        self._help_to_print = self.font_help.render(HELP_MSG, True, pg_color.THECOLORS['chocolate'], BG_COLOR)  
        self._text_to_print = self.font_text.render(INIT_MSG, True, pg_color.THECOLORS['blue'], BG_COLOR)  
    
    def set_text_to_print(self, message, color='blue'):
        """Create a surface for messages

        Args:
            message: String of the message
            color: String of the color (default = blue)
        """
        self._text_to_print = self.font_text.render(message, True, pg_color.THECOLORS[color], BG_COLOR)

    def render(self):
        """Display the game(labyrinth, peoples, items etc...)"""        
        #background color
        View.screen.fill(BG_COLOR)        

        # Draw the wall
        for wall in self.map._wall:
            x, y = wall.position            
            View.screen.blit(self.wall_img, (y * IMG_WIDTH, x * IMG_WIDTH))
        
        # Draw the hero
        x, y = self.map.hero.img_position        
        View.screen.blit(self.hero_img, (y, x))
        
        # Draw the guardian
        if self.guardian_img != None:
            x, y = self.map.end
            View.screen.blit(self.guardian_img, (y * IMG_WIDTH, x * IMG_WIDTH))

        # Draw the Items
        for item in self.map.items:
            x, y = item.img_position        
            View.screen.blit(item.img , (y, x))

        # Draw the messages surface        
        View.screen.blit(self._help_to_print, (1, 451))
        View.screen.blit(self._text_to_print, (1, 475))

        # Refresh
        pygame.display.flip()

            
        
