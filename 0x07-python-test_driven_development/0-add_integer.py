#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    This function adds 2 integers

    Args:
    a: The first integer to add
    b: the second integer to add

    Returns:
    The sum of a and b.

    Raises:
    TypeError: If a and b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

