""" Define a square based on size  """

class Square:
    """ square with private instance"""

    def __init__(self, size = 0):

        """ An argument where size: size of square """

        self.__size = size
    
    @property
    def square_size(self):
        """Applying the "getter" method to find size"""
        return self.__size
    
    @square_size.setter
    def square_size(self, size):
        """Applying the setter method to  validate that size is an integer that is greater than 0"""
        if type(size) == int:
            size
        else: 
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ defining a method that returns the current square area"""    
        return self.__size ** 2
    
    
#remember the deleter for later 


   