#!/usr/bin/python3
import sys

"""
     a function that executes a function safely
	otherwise - the result of the call to fct.
    """


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
