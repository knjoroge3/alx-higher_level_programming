#!/usr/bin/python3

"""
this code has a subclass
that inherits from the pyhton class
list
"""


class MyList(list):
    """
    class MyList that inherits from python
    list
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
