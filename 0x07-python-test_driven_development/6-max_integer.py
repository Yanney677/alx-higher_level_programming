#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    m = 1
    while m < len(list):
        if list[m] > result:
            result = list[m]
        m += 1
    return result
