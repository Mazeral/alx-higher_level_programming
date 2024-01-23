#!/usr/bin/python3
def safe_print_integer(value):
    value_cpy = str(value)
    try:
        if value_cpy.isdigit() or \
                (value_cpy.startswith('-') and value_cpy[1:].isdigit()):
            print("{:d}".format(value))
            return True
        else:
            return False
    except Exception:
        return False
