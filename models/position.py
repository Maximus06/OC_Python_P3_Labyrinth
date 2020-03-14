class Position:
    def __init__(self, x, y):
        self.position = (x, y)
    
    def __repr__(self):
        return str(self.position)
    
    def __hash__(self):
        """Pour pouvoir être utilisé en clé de dictionnaire """
        return hash(self.position)
    
    def __eq__(self, pos):
        return self.position == pos.position

    def __getitem__(self, index):
        """To be able to iterate or unpact"""
        return self.position[index]    

    # tout dépend comment on veut gérer les axes x et y. Ici c'est à la manière de numpy
    def up(self):
        x, y = self.position
        return Position(x-1, y)
    
    def down(self):
        x, y = self.position
        return Position(x+1, y)
    
    def right(self):
        x, y = self.position
        return Position(x, y+1)

    def left(self):
        x, y = self.position
        return Position(x, y-1)
