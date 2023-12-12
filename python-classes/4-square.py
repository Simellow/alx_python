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
    def size(self):
        """our getter simply retrieving our data"""
        return self.__size
    @size.setter
    def size(self, value):
        """Our setter that checks for type of value"""
        self.__size = value 
        if type(value) == int:
            value
        else: 
            raise TypeError("size must be an integer")
        
    def my_print(self):
        """method that prints the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
      