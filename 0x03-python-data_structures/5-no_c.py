#!/usr/bin/env python3
def no_c(my_string):
    dict = {ord(char): None for char in "cC"}
    new_string = my_string.translate(dict)
    return new_string
