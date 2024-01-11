#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not roman_string:
        return None
    for idx, char in enumerate(roman_string):
        if char == 'I' and (not roman_string[idx + 1] == False\
                and roman_string != 'V'):
            total = total + 1
        elif char == 'I' and roman_string[idx + 1] == 'V':
            total = total + 4
        elif char == 'I' and roman_string[idx] + 1 == 'X':
            total = total + 9
        elif char == 'V':
            total = total + 5
        elif char == 'X' and roman_string[idx + 1] == 'L':
            total = total + 40
        elif char == 'X' and roman_string[idx + 1] == 'C':
            total = total + 90
        elif char == 'X':
            total = total + 10
        elif char == 'L':
            total = total + 50
        elif char == 'C' and roman_string[idx + 1] == 'D':
            total = total + 400
        elif char == 'C' and roman_string[idx + 1] == 'M':
            total = total + 900
        elif char == 'C':
            total = total + 100
        elif char == 'D':
            total = total + 500
        elif char == 'M':
            total = total + 1000
    return total
