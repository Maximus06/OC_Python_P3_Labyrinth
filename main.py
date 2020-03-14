import pygame
from models.game import Game

# https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1400238-tp-dk-labyrinthe

if __name__ == '__main__':
    pygame.init()
    Game.run()
    pygame.quit()

