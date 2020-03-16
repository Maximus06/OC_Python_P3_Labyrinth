"""Module for the application contants"""

import os

# APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# app directory
APP_DIR = os.getcwd()

# Image directory
IMG_DIR = APP_DIR + '/images/'

# Image widht
IMG_WIDTH = 30

# Image Hero
IMG_HERO = IMG_DIR + 'MacGyver.png'
# Image Gardian
IMG_GARDIAN = IMG_DIR + 'guardian.png'
# Image wall
IMG_WALL = IMG_DIR + 'wall.png'
# Image tube
IMG_TUBE = IMG_DIR + 'tube.png'
# Image needle
IMG_NEEDLE = IMG_DIR + 'needle.png'
# Image ether
IMG_ETHER = IMG_DIR + 'ether.png'

# means for the char in the text file
PATH_CHAR = 'p'
WALL_CHAR = 'w'
START_CHAR = 'S'
END_CHAR = 'E'

if __name__ == "__main__":
    print(f'os.getcwd =', os.getcwd())
    print(f'IMG_DIR =', IMG_DIR)
