#!/usr/bin/python3
"""define a class Square"""


class Square:
    """implementation of class square"""

    def __init__(self, size=0):
        """initialisation a new square

        Args:
            size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square"""
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

    def __eq__(self, other):
        """define the comparision of Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define comparison Square not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define comparison Square is less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """define comparison Square is <="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define the comparison Square is greater"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define the compmarison Square >="""
        return self.area() >= other.area()
