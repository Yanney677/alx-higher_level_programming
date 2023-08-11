#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1
    z = number % 10
    print("{:d}".format(z), end="")
    return z
