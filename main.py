import pygame
from sys import exit
from models.game import Game

if __name__ == '__main__':
    pygame.init()
    Game.run()
    pygame.quit()    
    exit()

