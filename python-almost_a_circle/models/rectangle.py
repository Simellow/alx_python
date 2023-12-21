"""importing the class 'Base' """
from models.base import Base

class Rectangle(Base):
    """Defining our constructor with as our parameters"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Assign each argument to the right attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width where height input must be positive integer"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height where height input must be positive integer"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x where x input must be an integer and greater than 0"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ finds y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y where y input must be an integer and greater than 0"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    
    def area(self):
        """method that returns the area of the rectangle"""
        return self.__width * self.__height
    
    def display(self):
        """method that returns in stdout the Rectangle 
        instance with the character # for width and height"""
        for _ in range(self.height):
            print("#" * self.width)
    
    def __str__(self):
        """__str__ for rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    # [Rectangle] (<id>) <x>/<y> - <width>/<height>
    
    def display(self):
        """method that returns in stdout the Rectangle 
        instance with the character # for x and y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)
    
    def update(self, *args, **kwargs):
        """Updating key-worded arguments"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))