"""Module for the application contants and parameters setting"""

import os

# APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# app directory
APP_DIR = os.getcwd()

MAP_FILE = "labyrinth.txt"

# Image directory
IMG_DIR = APP_DIR + '/.ressources/images/'
# Sound directory
SOUND_DIR = APP_DIR + '/.ressources/sound/'
SOUND_VICTORY = SOUND_DIR + 'MacGyver.mp3'

# graphic librairy
GRAPH_LIB = 'pygame'

# Message
HELP_MSG = 'Press Q to Quit, F5 to reset, Arrow keys to move.'
INIT_MSG = 'MacGyver must pick up 3 objects before leaving.'
WIN_MSG = 'Good Game, you win!'
LOSE_MSG = 'GAME OVER! Missing objects:'

# Screen dimension
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500

# color
BG_COLOR = (230, 230, 230)
WIN_COLOR = 'darkcyan'
LOSE_COLOR = 'red'

# Image widht
IMG_WIDTH = 30

# tick by secondes
TICK = 20

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

# Image error (if not found)
IMG_ERROR = ('OOps, an error occurs cause a image file was not found. Error '
            'detail: ')

# means for the char in the text file
PATH_CHAR = 'p'
WALL_CHAR = 'w'
START_CHAR = 'S'
END_CHAR = 'E'
