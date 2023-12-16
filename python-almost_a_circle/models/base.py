"""Defining our class Base"""
class Base:

    """private instance attribute initialization"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for base"""
        self.id = id
        """if id is not "None", we assign self.id to id
        otherwise we update our private class attribute.
         We finally assign the new value to the public 
         instance attribute id"""
        if id is not None:
            self.id = id
        else: 
            Base.__nb_objects += 1
            self.id = self.__nb_objects