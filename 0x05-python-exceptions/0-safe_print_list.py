#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (integer, string): the list to print elements from.
        x (integer): The number of elements of my_list to print.

    Returns:
        the real number of elements printed.
    """
    result = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)

