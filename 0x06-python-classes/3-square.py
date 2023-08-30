#!/usr/bin/python3
"""define a class"""


class Square:
    """implementation of the class square"""

    def __init__(self, size=0):
        """initialisation of a new square

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
