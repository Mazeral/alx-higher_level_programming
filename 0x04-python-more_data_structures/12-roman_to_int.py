#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not roman_string:
        return None
    for i in roman_string:
        if i == 'I':
            total = total + 1
        elif i == 'V':
            total = total + 5
        elif i == 'X':
            total = total + 10
        elif i == 'L':
            total = total + 50
        elif i == 'C':
            total = total + 100
        elif i == 'D':
            total = total + 500
        elif i == 'M':
            total = total + 1000
    return total
