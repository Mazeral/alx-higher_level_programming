#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = str(my_list[i])
            if value.isdigit() or \
                    (value.startswith('-') and value[1:].isdigit()):
                print("{:d}".format(int(value)), end="")
                count += 1
        print()
        return count
    except (TypeError, ValueError):
        pass
    return count
