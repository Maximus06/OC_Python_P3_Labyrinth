"""This module contains the Game class."""

from sys import exit

import pygame

from .map import Map
from .hero import Hero
from .item import Item
from settings import (IMG_GARDIAN, IMG_WALL, IMG_WIDTH, IMG_NEEDLE, IMG_ETHER, IMG_TUBE, TICK,
                      WIN_COLOR, LOSE_COLOR, SOUND_VICTORY, WIN_MSG, LOSE_MSG)
from views.view import View
from .factory import create_view

class Game:
    """The Game class manages the game flow"""

    @classmethod
    def run(cls):
        """The run method is the main loop for the game."""        
        cls._init()

        cls.play = True
        cls.end_game = False
        while cls.play:
            #Limit the tick to x frames by secondes
            pygame.time.Clock().tick(TICK)
            cls._check_events()
            cls.view.render()        
    
    @classmethod
    def _init(cls):
        """The init method initialize the Map and View Object"""        
        cls.map = Map('labyrinth.txt')        
        # cls.view = View(cls.map)        
        cls.view = create_view(cls.map)        

    @classmethod
    def _check_events(cls):
        """Respond to keypresses events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.play = False
            elif event.type == pygame.KEYDOWN:
                cls._check_keydown_events(event)

    @classmethod
    def _check_keydown_events(cls, event):
        """Respond to keydown events"""
        if event.key == pygame.K_F5:
            pygame.mixer.music.stop()
            cls.reset()
        # Use unicode here cause pygame map in querty mode
        elif event.unicode == 'q' or event.unicode == 'Q':            
            cls.play = False
        elif event.unicode == 's' or event.unicode == 'S':                        
            pygame.mixer.music.stop()
        
        # game is over, we don't want to check the direction keys
        if cls.end_game:
            return
            
        if event.key == pygame.K_RIGHT:
            cls.map.hero.move('right')
        elif event.key == pygame.K_LEFT:
            cls.map.hero.move('left')
        elif event.key == pygame.K_UP:
            cls.map.hero.move('up')
        elif event.key == pygame.K_DOWN:
            cls.map.hero.move('down')            

        cls._check_collision()

    @classmethod
    def _check_collision(cls):
        """Manage Hero collisions with items and guardian"""
        hit_item, item_name = cls.map.items_collision()
        if hit_item:
            # message to print
            inventory = f'{cls.map.hero.item_number}/3'
            msg = f"MacGyver picked up {item_name}. ({inventory})"
            cls.view.set_text_to_print(msg)

        if cls.map.is_guardian_collision():
            cls._check_victory()

    @classmethod
    def _check_victory(cls):
        """Determine if the game is won or lost"""
        objects_victory = {'needle', 'tube', 'ether'}
        missing_objects = objects_victory - cls.map.hero.items        
        if len(missing_objects) == 0:            
            cls.view.set_text_to_print(WIN_MSG, WIN_COLOR)
            cls.view.guardian_img = None
            pygame.mixer.music.load(SOUND_VICTORY)
            pygame.mixer.music.play()
        else:            
            # cls.view.set_text_to_print(f'GAME OVER. Il te manquait {missing_objects}', LOSE_COLOR)
            cls.view.set_text_to_print(f'{LOSE_MSG} {missing_objects}', LOSE_COLOR)

        cls.end_game = True
    

    @classmethod
    def reset(cls):
        """This method launch a new game"""                
        del cls.map
        cls.run()



