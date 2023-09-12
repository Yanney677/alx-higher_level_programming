#!/usr/bin/python3
"""A module that checks if an object is an instance
or a specified class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an
        instance of the specified class; otherwise False
    Args:
        obj (obj): The object
        a_class (obj): The class
    Returns:
        boolean: if isinstance othewise false
    """

    return True if type(obj) is a_class else False
