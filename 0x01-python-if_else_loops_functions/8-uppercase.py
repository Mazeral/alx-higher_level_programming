#!/usr/bin/python3
def uppercase(str):
    for i, c in str:
        if ord(c) >= 97 and ord(c) <=122:
            str[i] = chr(ord(c) - 32)
    print("{}".format(str))
