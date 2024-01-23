def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(int(my_list[i]), end='')
            count+=1
        print("")
    except (IndexError, TypeError):
        pass
    return count
