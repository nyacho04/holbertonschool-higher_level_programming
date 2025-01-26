#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    a = 0
    while a < x:
        try:
            print("{:d}".format(my_list[a]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        a += 1
    print()
    return count
