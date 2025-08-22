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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gettin width so that I can  proceed to set it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting width and checking is it is an int or great than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getting height so that I can proceed to set it
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setting height and checking if it is an int and greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculates the area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculates the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            summation = (self.__width + self.__height)
            return (summation * 2)

    def __str__(self):
        result = ''
        a = ''
        if (self.__width == 0) or (self.__height == 0):
            return ('')
        else:
            for i in range(self.__height):
                for item in range(self.__width):
                    a = '#'
                    result += a
                if i != self.__height - 1:
                    result += '\n'
        return (result)


rectangle = Rectangle()  # instantiating the object
