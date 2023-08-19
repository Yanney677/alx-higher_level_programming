#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_of_lst = list(a_dictionary.keys())

    for value_of_dict in keys_of_lst:
        if value == a_dictionary.get(value_of_dict):
            del a_dictionary[value_of_dict]

    return (a_dictionary)
