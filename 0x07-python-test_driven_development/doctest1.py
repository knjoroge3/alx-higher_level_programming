#!/usr/bin/python3

import doctest

"""
this program tries to use doctest
a class and call objects so that we
can understand if doctest will work.
"""

class Math:
    """
    class that will compute math
    """

    def __init__(self, a, b):
        """
        this constructor accepts two values a and b
        """
        self.a = a
        self.b = b

    def Mult(self):
        """
        this mult takes in two variables and computes them
        to find multiplication.
        >>> Math(2, 3).Mult()
        6
        """
        return self.a * self.b

    def Add(self):
        """
        this function adds two numbers
        >>> Math(2, 3).Add()
        5
        """

        return self.a + self.b

    def __str__(self):
        """
        Prints the values instead of the memory address
        """
        
        return("{} {}".format(self.a, self.b))

multiplication_result = Math(5, 8)
Addition = Math(50, 100)

print("The results of the multiplication is {}".format(multiplication_result.Mult()))
print("The results of the addition is {}".format(Addition.Add()))
