#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, ValueError):
        pass
        result = None
    finally:
        if result is None:
            print("Inside result: None")
        else:
            print("Inside result: {}".format(result))
