#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif my_list[idx]:
        return my_list[idx]
    else:
        return None
