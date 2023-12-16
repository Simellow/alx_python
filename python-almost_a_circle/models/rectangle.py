"""using the import method to import
the class Base"""
Base = __import__('base').Base

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
        """setter for width"""
        self.__width = value
    # width got and set

    @property
    def height(self):
        """getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value
    # height got and set

    @property
    def x(self):
        """getter for x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value
    # x got and set

    @property
    def y(self):
        """getter for y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setter for height"""
        self.__y = value
    # y got and set
    
    


