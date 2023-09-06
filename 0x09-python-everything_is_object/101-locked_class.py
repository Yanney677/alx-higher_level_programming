#!/usr/bin/python3
"""define a LockedClass."""


class LockedClass:
    """
    __slots__: Prevent the user from instantiating new LockedClass
    attributes called 'first_name'.
    """

    __slots__ = ("first_name",)
