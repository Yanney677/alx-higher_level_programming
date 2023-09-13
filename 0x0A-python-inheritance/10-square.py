#!/usr/bin/python3
"""A module that define the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Class Rectangle but takes a square
    """

    def __init__(self, size):
        """Initialize a square
            Args:
                size (int): size of square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
