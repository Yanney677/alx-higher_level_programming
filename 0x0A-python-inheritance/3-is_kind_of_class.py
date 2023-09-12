#!/usr/bin/python3

"""A function that checks if an object is an instance of a
class or of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise False
    Args:
        obj (obj): The object
        a_class (obj): The class
    Returns:
        boolean: if isinstance othewise false
    """

    return True if isinstance(obj, a_class) else False
