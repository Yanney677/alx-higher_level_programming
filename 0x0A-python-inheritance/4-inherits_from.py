#!/usr/bin/python3
"""Function that determines if an object is an instance of a
class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj (obj): The object
        a_class (obj): The class
    Returns:
        boolean: if isinstance othewise false
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False
