#!/usr/bin/python3

"""
Write an empty class Rectangle that defines a rectangle
You are not allowed to import any module
"""


class Rectangle:
    """
    an instance of the Rectangle Class
    """
    def __init__(self, width=0, height=0):
        """
        the initialization step
        """
        self.__width = width
        self.__height = height

    @property
    def width(self, value):
        """
        gettin width so that I can  proceed to set it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting width and checking is it is an int or great than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @property
    def height(self, value):
        """
        Getting height so that I can proceed to set it
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setting height and checking if it is an int and greater than 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height


rectangle = Rectangle()  # instantiating the object
