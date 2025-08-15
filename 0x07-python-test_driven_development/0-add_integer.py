#!/usr/bin/python3

"""
Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats,
otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module

"""

def add_integer(a, b=98):
    """
    function that adds two integers.
    varaible b is set first to 98
    """
    if isinstance(a, (int, float)):
        a = int(a)
        """
        this tests if the value a equals to a float or an int
        
        >>> if a != isinstance(a, (int, float)):
            print("a is neither a float or an int")
        """
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)

        """
        this tests if the value b equals to a float or an int

        >>> if b != isinstance(b, (int, float)):
            print("b is neither a float or an int")
        """
    else:
        raise TypeError("b must be an integer")

    return (a + b)
