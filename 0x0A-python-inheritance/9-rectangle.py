#!/usr/bin/python3
"""A module that holds the class BaseGeometry
"""


class BaseGeometry:
    """Initialize a class BaseGeometry
    """

    def area(self):
        """Calculate the area
            Returns:
                int: area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate input function passed
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initialize the class
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle
            Returns:
                int: area rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description
            Returns:
                str: rectangle description
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
