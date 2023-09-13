#!/usr/bin/python3
""" adds all arguments to a Python
    list, and then save them to a file:
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(arg, filename):
    if (os.path.exists(filename)):
        data = load_from_json(filename)
    else:
        data = []
    data.extend(arg)
    save_to_json(data, filename)


if __name__ == "__main__":
    arg = sys.argv[1:]
    filename = "add_item.json"
    add_item(arg, filename)
