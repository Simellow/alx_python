# class Animal:
    
#     alive = True

#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         print("this animal is eating")
#     def sleep(self):
#         print("this animal is sleeping")

# class Rabbit(Animal):
   
#     # using a method overriding to override the eat method
#     def eat(self):
#         print("this rabbit is eating a carrot")
   
#     def run(slef):
#         print("this rabbit is running")

# class Fish(Animal):
    
#     def swim(self):
#         print("this fish is swimming")

# class Eagle(Animal):
    
#     def fly(self):
#         print("this eagle is flying")

# rabbit = Rabbit()
# fish = Fish()
# eagle = Eagle()

# print(rabbit.alive)
# fish.eat()
# eagle.sleep()

# rabbit.run()
# fish.swim()
# eagle.fly()

# rabbit.eat()


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
