"""This module contains the main function for the MacGyver Game."""

from sys import exit

import pygame

from controllers.game import Game


def main():
    """This function is the main function of the game."""
    pygame.init()

    try:
        Game.run()
    except FileNotFoundError as err:
        print(err.args[0])

    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
