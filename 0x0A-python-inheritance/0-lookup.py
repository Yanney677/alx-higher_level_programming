#!/usr/bin/python3
""" Create a module of a list of available
    attributes and methods of an object:
"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object
    Args:
        obj(obj) - the object
    Returns:
        list: list of every attributes and methods
    """

    return dir(obj)
