#!/usr/bin/python3
"""A function that writes an Object to a
    text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename=""):
    """function that writes an Object
        to a text file, using a JSON
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
