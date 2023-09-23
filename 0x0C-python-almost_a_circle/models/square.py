#!/usr/bin/python3 # Tasks 10
"""Define a module for the class Square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Initailsation of the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Set the superclass constructor with id, x, y, width, and height"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation for the Square."""
        return '[()] ({}) {}/{} - {}'.\
            format(type(self).__name__.self,id, self.x, self.y, self.width)

    @property
    def size(self):
        """Set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square, Update both width and height."""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Updates instances attributes"""
        if id is not None:
            self.id = id
        if size is not None;
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update attributes with arguments (both key-worded and non-key-worded)."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dict. representation of this class"""
        return ("id": self.id, "width": self.__width, "height": self.__height, 
                "x": self.__x, "y": self.___y)
