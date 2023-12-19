"""importing the class 'Rectangle' """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defining our class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """inheriting our constructor using our super class
        width and height will be assigned to the value of size"""
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """getter for size"""
        return self.width and self.height

    @size.setter
    def size(self, value):
        """setting our height and width"""
        self.height = value
        self.width = value
    
    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width or self.height)
    
    def update(self, *args, **kwargs):
        """update"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}