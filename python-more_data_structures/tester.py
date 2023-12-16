class Animal:
    
    alive = True

    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
   
    # using a method overriding to override the eat method
    def eat(self):
        print("this rabbit is eating a carrot")
   
    def run(slef):
        print("this rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("this fish is swimming")

class Eagle(Animal):
    
    def fly(self):
        print("this eagle is flying")

rabbit = Rabbit()
fish = Fish()
eagle = Eagle()

print(rabbit.alive)
fish.eat()
eagle.sleep()

rabbit.run()
fish.swim()
eagle.fly()

rabbit.eat()


class Rectangle:
    #parent with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
        

class Cube(Rectangle):
    #init inherits length and width via super
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
    #method that calculates the volume of a cube
        return self.length * self.width * self.height

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
    #method that calculates the ares of a square
        return self.length * self.width

cube = Cube(3, 3, 3)
square = Square(3, 3)

print(cube.volume())
print(square.area())


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print("{}: {}".format(key, value), end=" ")
    print("{}".format(kwargs.get("zip")))
    print("{} {}, {}".format(kwargs.get("address"), kwargs.get("street"), kwargs.get("zip")))


shipping_label("Simelo", "Aberra", "Bekele", 
               address = "123", street = "fakestreet", zip = "1883")

"""given an instance where you don't want to print the None 
if a key doesn't exist use an if else statement and
pecify what you want it to print instead"""


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
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
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
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be an integer')
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
    
    


