#!/usr/bin/python3
"""A function that returns
    the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):
        Args:
            my_obj (obj): object
        Returns:
            json: json object representation
    """
    return json.dumps(my_obj)
