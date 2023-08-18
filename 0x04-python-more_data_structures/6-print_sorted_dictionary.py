#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    alphaord_lst = list(a_dictionary.keys())
    alphaord_lst.sort()
    for i in alphaord_lst:
        print("{}: {}".format(i, a_dictionary.get(i)))
