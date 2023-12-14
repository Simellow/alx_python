""" function that returns true if the obj is exactly an instance of the specified class and false otherwise"""

def is_kind_of_class(obj, a_class):
    """ returns True if object is an instance of the
    using the is instance method"""
    return isinstance(obj, a_class)