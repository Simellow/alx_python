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

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


# r = Rectangle(3, 5)

# print(r)
# print(dir(r))

# try:
#     print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r2 = Rectangle(4, True)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
