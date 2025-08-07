#!/usr/bin/python3

"""
This module has a class square that checks both type and vallue
error of the oject
"""


class Square:
    """
    This is a class Square that checks the size attribute properly
    """
    def __init__(self, size=0):
        """
        Constructor that initializes size with type and value checks.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
