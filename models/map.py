from random import randint
import os
from .position import Position
from settings import PATH_CHAR, WALL_CHAR, START_CHAR, END_CHAR

class Map:
    def __init__(self, file_name):
        self.file_name = file_name

    # paths, walls, start(hero), end(guardian) and items position
        self._paths = set()
        self._start = set()
        self._end = set()
        self._wall = set()
        self._items = set()

        self.load_from_file()

    def __contains__(self, position):
        """Check if a position is in paths set. (is a valid path)."""
        return position in self._paths

    @property
    def start(self):
        return list(self._start)[0]

    @property
    def end(self):
        return list(self._end)[0]

    def is_valid_path(self, position):
        return position in self._paths

    def load_from_file(self):
        """Load the map structure from file."""
        with open(self.file_name) as infile:
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
    
    def get_item_position(self):
        """Return a random position for an item.
        The position returned must be in the valid path positions.
        Hero, guardian and already affected items position are excluded.

        Return pos: a Position object
        """

        # Take the valid position path minus Start, End and items position
        valid_pos_item = self._paths - self._start - self._end - self._items
        len_pos_item = len(valid_pos_item)        
        position = randint(0, len_pos_item - 1)        
        pos = list(valid_pos_item)[position]
        # Add this position to the items set to not choose it next call
        self._items.add(pos)

        return pos

def main():    
    my_map = Map('labyrinth.txt')
    
    # print("set of wall")
    # print(my_map._wall)
    print('start', my_map.start, type(my_map.start))
    print('end', my_map._end, type(my_map._end))

    my_map.get_item_position()
    my_map.get_item_position()
    my_map.get_item_position()

    print(f'\nos.getcwd =', os.getcwd())

if __name__ == '__main__':
    main()







