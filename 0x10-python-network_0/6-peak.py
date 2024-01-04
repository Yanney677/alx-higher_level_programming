#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """returns peak_size of the list"""
    if list_of_integers == []:
        return None

    peak_size = len(list_of_integers)
    if peak_size == 1:
        return list_of_integers[0]
    elif peak_size == 2:
        return max(list_of_integers)

    mid_size = int(peak_size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid_size - 1] and peak > list_of_integers[mid_size + 1]:
        return peak
    elif peak < list_of_integers[mid_size - 1]:
        return find_peak(list_of_integers[:mid_size])
    else:
        return find_peak(list_of_integers[mid_size + 1:])
