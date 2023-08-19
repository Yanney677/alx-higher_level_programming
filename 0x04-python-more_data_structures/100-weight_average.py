#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_lst = 0
    t = 0

    for tupse in my_list:
        num_lst += tupse[0] * tupse[1]
        t += tupse[1]

    return (num_lst / t)

