""" Define a square based on size  """

class Square:
    """ square with private instance"""

    def __init__(self, size = 0):

        """ An argument where size: size of square """

        self.__size = size
        if type(size) == int:
            size
        else: 
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """ defining a method that returns the current square area"""    
        return self.__size ** 2
    
    @property
    def square_size(self):
        """Applying the getter method"""
        return self.__size
    
    @square_size.setter
    def square_size(self, value):
        """Applying the setter method"""
        self.__size = value



    # def get_size(self):
    #     """Applying the getter method"""
    #     return self.__size
    
    # def set_name(self, new__size):
    #     """Applying the setter method"""
    #     self.__size = new__size
        