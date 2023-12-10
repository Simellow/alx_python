# class People:
     
#      Population = 0
     
#      def __init__(self, nickname, height, weight):
#         self.nickname = nickname
#         self.height = height
#         self.weight = weight 

#         print("Adding {}". format(self.nickname))

#         People.Population += 1
     
#      def introduce(self):
#         """ Python docstrings are strings used right after the 
#         definition of a function, method, class, or module """

#         """We can access the class docstring at runtime using People.__doc__ and the method docstring as People.introduce.__doc__"""

#         print("This is {}. I am {}cms, and I weigh {}kgs.".format(self.nickname, self.height, self.weight))
    
#      def remove(self):
#          print("{} is gone". format(self.nickname))
         
#          People.Population -= 1 
         
#          if People.Population == 0:
#              print("There are no more people in here") 
#          else:
#              print("There are {:d} people in here".format(People.Population))
     
#     #  how_many = classmethod(how_many)???
#      @classmethod
#      def  how_many(cls):
#          print ("\nThere are {:d} people at the moment.\n".format(People.Population))
        

# Person_1 = People("Simo", 165, 48)
# Person_2 = People("Leli", 170, 45)

# Person_1.introduce()


# Person_2.introduce()
# People.how_many()

# print("\nThe people are in the office getting work done...\n")

# print("\nSometime later....\n")

# print("Everyone is finished")

# Person_1.remove()
# Person_2.remove()

# People.how_many

# """All class members are public. One exception: 
# If you use data members with names using the double underscore prefix such as __privatevar,
#  Python uses name-mangling to effectively make it a private variable.

# Thus, the convention followed is that any variable that is to be used only within the class or object 
# should begin with an underscore and all other names are public and can be used by other classes/objects. 
# Remember that this is only a convention and is not enforced by Python (except for the double underscore prefix)"""

class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
u.name