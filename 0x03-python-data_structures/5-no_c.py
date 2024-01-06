#!/usr/bin/env python3
def no_c(my_string):
    for i, x in enumerate(my_string):
        if x == 'c':
            del(my_string[i])
    return new_string
