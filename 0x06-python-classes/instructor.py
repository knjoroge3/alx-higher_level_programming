#!/usr/bin/python3

"""
this code shows the how of creating a class
object and an attribte and calling the attributes
so they can be printed
"""

class Instructor:
    """
    a class instructor
    """
    def __init__(self):
        print("Creating a new object")


instructor_1 = Instructor()
instructor_1.name = "Kennedy"
print(instructor_1.name)
