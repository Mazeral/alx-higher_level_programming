#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            pass
            print("division by 0")
            value = 0
        except IndexError:
            pass
            print("out of range")
            value = 0
        except TypeError:
            pass
            print("wrong type")
            value = 0
        finally:
            result.append(value)
    return result
