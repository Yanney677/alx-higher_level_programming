#!/usr/bin/python3
"""A function that reads a text file
UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
        Args:
            filename (str): name of the file
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
