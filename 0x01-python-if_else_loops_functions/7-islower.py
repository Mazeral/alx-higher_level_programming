#!/usr/bin/python3
def islower(c):
    if int(ord(c)) < 97:
        print("{} is upper".format(c))
        return False
    else:
        print("{} is lower".format(c))
        return True
