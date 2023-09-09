#!/usr/bin/python3
"""defines the matrix division function"""

def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix

    Args:
    matrix: a list of integers or floats
    div: a number(integer or float)

    Returns:
    a new matrix with elements rounded to 2 decimal places

    Raises:
    TypeError: if matrix is not list of lists of integers or floats
    TypeError: if each row of the matrix is not the same size
    TypeError: if div is not a number(integer or float)
    ZeroDivisionError: if div by 0 or is equal to 0
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
