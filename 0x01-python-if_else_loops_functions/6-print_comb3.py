#!/usr/bin/python3
for first number in range(0, 10):
    for second number in range(first number + 1, 10):
        if first number == 8 and second number == 9:
            print("{}{}".format(first number, second number))
        else:
            print("{}{}".format(first number, second number), end=", ")


