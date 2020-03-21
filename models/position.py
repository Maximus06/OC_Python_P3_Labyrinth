"""This module contains the Position class"""

class Position:
    """Represent a position object with x and y coordinates"""    
    def __init__(self, x, y):
        self.position = (x, y)
    
    def __repr__(self):
        """Return a String representation of the position"""
        return str(self.position)
    
    def __hash__(self):
        """Return a hash of the position tuple"""
        return hash(self.position)
    
    def __eq__(self, pos):
        """Return True if the compare position is egal to this object"""
        return self.position == pos.position

    def __getitem__(self, index):
        """To be able to iterate or unpact"""
        return self.position[index]    

    # Coordinate x are columns and y are lines (numpy way)
    def up(self):
        """Move position up."""
        x, y = self.position
        return Position(x-1, y)
    
    def down(self):
        """Move position down."""
        x, y = self.position
        return Position(x+1, y)
    
    def right(self):
        """Move position right."""
        x, y = self.position
        return Position(x, y+1)

    def left(self):
        """Move position left."""
        x, y = self.position
        return Position(x, y-1)
