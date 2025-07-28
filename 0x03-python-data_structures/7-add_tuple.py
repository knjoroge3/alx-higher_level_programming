#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    if len(tuple_a) > 0:
        i = tuple_a[0]
    else:
        i = 0
    if len(tuple_a) > 1:
        j = tuple_a[1]
    else:
        j = 0
    if len(tuple_b) > 0:
        k = tuple_b[0]
    else:
        k = 0
    if len(tuple_b) > 1:
        m = tuple_b[1]
    else:
        m = 0

    return (i + k, j + m)
