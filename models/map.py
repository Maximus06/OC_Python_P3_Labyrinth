"""This module contains the Map class"""

from random import randint

from settings import (PATH_CHAR, WALL_CHAR, START_CHAR, END_CHAR, IMG_ETHER,
                      IMG_NEEDLE, IMG_TUBE)
from .hero import Hero
from .item import Item
from .position import Position


class Map:
    """This class represents the labyrinth

    Public Attributes:
        - start: start position for the hero
        - end: end position is the end position for the game and the position
        for the guardian.
        - hero: return the hero.
        - items: return the labyrinth items
        - walls: return a set of walls position.

    Public Methods:
        - is_valid_path: check if a position is a valid path
        - get_random_position: Return a random position in the valid paths.
        - items_collistion: handle the collisions between hero and items.
        - is_guardian_collision: return True if the hero meet the guardian.
    """

    def __init__(self, file_name):
        """Initialize the map attributes

        Args:
            file_name: String of the text file containing the structure of the
            labyrinth.
        """
        self._file_name = file_name

    # paths, walls, start(hero), end(guardian) and items position
        self._paths = set()
        self._start = set()
        self._end = set()
        self._wall = set()

        # Load the structure of the labyrinth
        self._load_from_file()

        # MacGyver
        self._hero = Hero(self)

        # The items
        self._items = []
        # To mémorize the items position already created
        self._items_created = set()
        self._create_items()

    def __contains__(self, position):
        """Return True if a position is in paths set. (is a valid path)."""
        return position in self._paths

    @property
    def hero(self):
        """Return the Hero object."""
        return self._hero

    @property
    def items(self):
        """Return a List of map Items."""
        return self._items

    @property
    def start(self):
        """Return a Position object for the hero start position."""
        return list(self._start)[0]

    @property
    def end(self):
        """Return a Position object for the guardian position."""
        return list(self._end)[0]

    @property
    def wall(self):
        """Return a set of wall position"""
        return self._wall

    def is_valid_path(self, position):
        """Return True if the position given is a valid path."""
        return position in self._paths

    def _load_from_file(self):
        """Load the map structure from file."""
        try:
            with open(self._file_name) as infile:
                for x, line in enumerate(infile):
                    for y, char in enumerate(line):
                        if char == PATH_CHAR:
                            self._paths.add(Position(x, y))
                        elif char == WALL_CHAR:
                            self._wall.add(Position(x, y))
                        elif char == START_CHAR:
                            self._paths.add(Position(x, y))
                            self._start.add(Position(x, y))
                        elif char == END_CHAR:
                            self._paths.add(Position(x, y))
                            self._end.add(Position(x, y))
        except FileNotFoundError:
            msg = 'The game could not be loaded because the file '
            msg += f'{self._file_name} was not found.'
            raise FileNotFoundError(msg)

    def get_random_position(self):
        """Return a random position for an item.

        The position returned must be in the valid path positions.
        Hero, guardian and already affected items position are excluded.

        Return pos: a Position object
        """

        # Take the valid position path minus Start, End and items position
        valid_pos_item = self._paths - self._start - self._end \
            - self._items_created

        len_pos_item = len(valid_pos_item)
        position = randint(0, len_pos_item - 1)
        pos = list(valid_pos_item)[position]
        # Add this position to the items set to not choose it next call
        self._items_created.add(pos)

        return pos

    def _create_items(self):
        """Create the 3 items on the maps"""
        needle = Item(self, IMG_NEEDLE, 'needle')
        self._items.append(needle)
        ether = Item(self, IMG_ETHER, 'ether')
        self._items.append(ether)
        tube = Item(self, IMG_TUBE, 'tube')
        self._items.append(tube)

    def items_collision(self):
        """Manage hero collisions with items.
        Return True and item name if a collision occurs between hero and and
        item.
        """
        for item in self._items:
            if item.position == self._hero.position:
                # Add the item to the items hero
                self._hero.items = item.name
                # Del the item from the map
                self._items.remove(item)
                return (True, item.name)
        return (False, '')

    def is_guardian_collision(self):
        """Return True if hero hits guardian else false."""
        if self._hero.position == self.end:
            return True
        return False
