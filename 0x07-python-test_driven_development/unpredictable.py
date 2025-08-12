#!/usr/bin/pyhton3

import doctest

"""
This program tries to show how
an unpredictable behaviour such as the 
memory address allocation of a computer
can still be tested.
"""

class Unpredictable:
    pass


def unpredicatble(obj):
    """
    returns a new list containing obj

    >>> unpredictable(Unpredicatble()) #doctest: +ELLIPSIS
     [<doctest_unpredictable.Unpredictable object at 0x...>]
     """
