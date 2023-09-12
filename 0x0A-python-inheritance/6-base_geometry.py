#!/usr/bin/python3
"""A modulethat has an empty base class BaseGeometry
   and empty class function
"""


class BaseGeometry:
    """initalize a class BaseGeometry
    """

    def area(self):
        """calculate the area
            Returns:
                int: area
        """
        raise Exception("area() is not implemented")
