"""This module contains the main function for the MacGyver Game."""

from sys import exit

import pygame

from models.game import Game

def main():
    """This function launch the game."""
    pygame.init()
    Game.run()
    pygame.quit()    
    exit()

if __name__ == '__main__':
    main()

