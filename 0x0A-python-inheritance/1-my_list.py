#!/usr/bin/python3
"""
Create a class MyList that inherits from list
"""


class MyList(list):
    """inherits from the class list"""

    def __init__(self):
        """initialize the object
        """
        super().__init__()

    def print_sorted(self):
        """prints the sorted list
        """
        print(sorted(self))
