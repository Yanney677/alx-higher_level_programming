#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    nos = 0

    for i in uniq_lst:
        nos += i

    return (nos)
