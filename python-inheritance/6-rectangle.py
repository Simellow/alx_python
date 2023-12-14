"""class called BaseGeometry"""

class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """Raising exception"""
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        """to check for positive integer """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))



class Rectangle(BaseGeometry):
    """class  Rectangle that inherits from BaseGeometry"""
    
    def __init__(self, width, height):
       
        """Validating rectangle from BaseGeometry"""

        self.integer_validator('', width)
        self.integer_validator('', height)
        self.__width = width
        self.__height = height
        