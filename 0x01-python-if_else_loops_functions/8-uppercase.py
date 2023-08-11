#!/usr/bin/python3
def uppercase(str):
    for z in range(len(str)):
        a = ord(str[z])
        if (a >= 97 and a <= 122):
            a -= 32
        print("{}".format(chr(a)), end="")
    print()
