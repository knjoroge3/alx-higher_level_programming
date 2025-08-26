#!/usr/bin/python3

"""
An Empty class base
"""


class BaseGeometry:
    """
    An empty class defination
    """
    def area(self):
        raise Exception("area() is not implemented")


base = BaseGeometry()
