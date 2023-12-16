"""using the import method to import
the class Base"""
from models.base import Base

"""our subclass Rectangle
that inherits from the parnet class Base"""
class Rectangle(Base):

    """Defining our constructor with as our parameters"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Assign each argument width, height, x and y 
        to the right attribute"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    
    @property
    def width(self):
        """getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for width where height input must be positive integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    # width got and set

    @property
    def height(self):
        """getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for height where height input must be positive integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    # height got and set

    @property
    def x(self):
        """getter for x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter for x where x input must be an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    # x got and set

    @property
    def y(self):
        """getter for y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setter for y where y input must be an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    # y got and set
    
    


