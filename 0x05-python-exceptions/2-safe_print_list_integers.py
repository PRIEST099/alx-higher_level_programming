#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            printed += 1
            if printed == x:
                break
        except (ValueError, TypeError):
            continue
    print()
    return printed
