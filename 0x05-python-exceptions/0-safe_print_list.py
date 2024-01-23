def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if i < len(my_list):
                print(my_list[i], end=" ")
                count += 1
        print()
    except Exception as e:
        pass
    return count
