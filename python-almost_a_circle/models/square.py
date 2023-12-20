"""importing the class 'Rectangle' """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defining our class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """inheriting our constructor using our super class
        width and height will be assigned to the value of size"""
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting our height and width to equal values"""
        self.height = value
        self.width = value
    
    def __str__(self):
        """__str__ for square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    