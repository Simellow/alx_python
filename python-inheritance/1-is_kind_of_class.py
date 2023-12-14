"""function that returns true if the obj is exactly an instance of the specified class and false otherwise"""
def is_same_class(obj, a_class):
   """ returns True if object is an instance of the
    class or of a class that class inherited from """
   return isinstance(obj, a_class)