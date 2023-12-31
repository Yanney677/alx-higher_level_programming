#!/usr/bin/python3
""" that inserts a line of text to a file, after
    each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ that inserts a line of text to a file, after
        each line containing a specific string
    """
    modified_str = ""
    with open(filename, encoding="utf8") as myFile:
        for line in myFile:
            modified_str += line
            if search_string in line:
                modified_str += new_string

    with open(filename, mode="w") as myFile:
        myFile.write(modified_str)
