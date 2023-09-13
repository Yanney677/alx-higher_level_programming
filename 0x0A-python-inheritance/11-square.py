#!/usr/bin/python3
"""A module that holds the class BaseGeometry
"""


class BaseGeometry:
    """Initialize the class BaseGeometry
    """

    def area(self):
        """Calculate the area
            Returns:
                int: area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input function passed
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from the class BaseGeometry
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
        """Calculate area of the rectangle
            Returns:
                int: area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description
            Returns:
                str: rectangle description
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Inherit from Rectangle but takes a square
    """

    def __init__(self, size):
        """Initialize a square
            Args:
                size (int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns square description
            Returns:
                str: square description
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
