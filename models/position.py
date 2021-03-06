"""This module contains the Position class"""


class Position:
    """Represent a position object with x and y coordinates.

    Properties:
        - position: return the position (x, y).

    Public Methodes:
        - up: move the postion up.
        - down: move the postion down.
        - left: move the postion left.
        - right: move the postion right.
    """

    def __init__(self, x, y):
        self._position = (x, y)

    def __repr__(self):
        """Return a String representation of the position"""
        return str(self._position)

    def __hash__(self):
        """Return a hash of the position tuple"""
        return hash(self._position)

    def __eq__(self, pos):
        """Return True if the compare position is egal to this object"""
        return self._position == pos.position

    def __getitem__(self, index):
        """To be able to iterate or unpact"""
        return self._position[index]

    @property
    def position(self):
        """Return the tuple of position (x,y)."""
        return self._position

    # Coordinate x are columns and y are lines (numpy way)
    def up(self):
        """Move position up."""
        x, y = self._position
        return Position(x - 1, y)

    def down(self):
        """Move position down."""
        x, y = self._position
        return Position(x + 1, y)

    def right(self):
        """Move position right."""
        x, y = self._position
        return Position(x, y + 1)

    def left(self):
        """Move position left."""
        x, y = self._position
        return Position(x, y - 1)
