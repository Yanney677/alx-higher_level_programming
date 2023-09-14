#!/usr/bin/python3
"""returns a list of lists of integers
    representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    pt_num = []
    for num in range(1, n + 1):
        A = 1
        row = []
        for s in range(1, num + 1):
            row.append(A)
            A = A * (num - s) // s
        pt_num.append(row)
    return pt_num
