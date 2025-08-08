#!/usr/bin/python3

"""
Write a class Square that defines a square.
"""


class Square:
    """
    the blue print of the object square
    """
    def __init__(self, size=0):
        """
        Constructor that initializes size with type and value checks
        """
        self.size = size

    @property
    def size(self):
        """
        return the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
