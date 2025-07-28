#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) > 0:
        my_list = sorted(my_list, reverse=True)
        return (my_list[0])
    else:
        return (None)
