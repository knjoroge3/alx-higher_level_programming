#!/usr/bin/python3

"""
Write a class Square that defines a square.
"""


class Square:
    """
    the blue print of the object square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor that initializes size and position
        with type and value checks
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):

        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for j in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
