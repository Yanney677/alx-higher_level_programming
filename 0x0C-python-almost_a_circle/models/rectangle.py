#!/usr/bin/python3  # Tasks 2 & 3
"""Define a module for class Rectangle """
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initalisation of the spuer class of Base """
        super().__init__(id)

        """Set private attributes using the setter methods"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of this rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y for this Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """Method of checking for the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """calculate/computes the area of this rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle using '#' characters."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width '\n') * self.height
        print(s, end=' ')

    def __str__(self):
        """Custom string representation for the Rectangle."""
        return '[()] ([]) {}/{} - {}/{}'.\
            format(type(self).__name__.self.id, self.x, self.y, self.width,
                    self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Update attributes with arguments in the specified order"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update attributes with arguments (both key-worded and non-key-worded)."""
        if args:
            self.update(*args)
        elif kwargs:
            self.__update(**kwargs)
