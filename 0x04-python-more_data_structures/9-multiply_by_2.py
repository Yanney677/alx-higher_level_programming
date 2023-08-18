#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_directory = a_dictionary.copy()
    keys_lst = list(new_directory.keys())

    for i in keys_lst:
        new_directory[i] *= 2

    return (new_directory)
