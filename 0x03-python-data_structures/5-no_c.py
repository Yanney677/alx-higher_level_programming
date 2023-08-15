#!/usr/bin/python3
def no_c(my_string):
    remove_string = my_string.translate({ord(i): None for i in 'cC'})
    return remove_string
