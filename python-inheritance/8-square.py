"""contains subclass Square
which inherits from class Rectangle """

Rectangle = __import__('7-rectangle').Rectangle
    
class Square(Rectangle):
    """ defines class Square """

    def __init__(self, size):
        """ initializes empty Square and
        validates size as a positive integer """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)