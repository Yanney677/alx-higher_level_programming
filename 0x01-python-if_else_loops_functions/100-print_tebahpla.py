#!/usr/bin/python3
for z in range(122, 96, -1):
    if (z % 2 != 0):
        z -= 32
    print("{}".format(chr(z)), end="")
