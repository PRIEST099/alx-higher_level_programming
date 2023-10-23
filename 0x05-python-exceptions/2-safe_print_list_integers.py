#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for i in my_list:
        try:
            if printed >= x:
                break
            if isinstance(i, int):
                print("{:d}".format(i), end="")
        except Exception:
            break
    print()
    return printed
