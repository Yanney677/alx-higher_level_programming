#!/usr/bin/python3
"""A module that holds the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherit from BaseGeometry
    """

    def __init__(self, width, height):
        """Initialize of the class
            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
