#!/usr/bin/python3
"""define a class"""


class Square:
    """iplementation of class square"""

    def __init__(self, size):
        """initialisation of  new square

        Args:
            size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Set the current square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square area with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
