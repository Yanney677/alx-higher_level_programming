#!/usr/bin/python3
"""A function that creates an Object from a "JSON file"
"""
import json


def load_from_json_file(filename=""):
    """function that creates an Object from a "JSON file"
    """
    with open(filename, encoding="utf-8") as myFile:
        my_obj = json.load(myFile)

    return my_obj
