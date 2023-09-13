#!/usr/bin/python3
"""
    Defines the student class
"""


class Student:
    """
        Defines the student class
    """

    def __init__(self, first_name, last_name, age):
        """
            Initialize the instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Create a dict reprenting the class
        """
        return (self.__dict__)
