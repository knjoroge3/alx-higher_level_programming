#!/usr/bin/python3

"""
this code attempts to explain
the difference between class variables
and the ojbect variables
"""


class Robot:

    population = int(input("How may robots do you have? "))
    # this is a class variable
    #  it is available in the class and can be used wherever
    #  in the class

    def __init__(self, name):
        self.name = name  # this is an object variable and will only be
        #  accessed using the object only
        #  the best way to distinguish between
        #  an object variable is that the calling of the
        #  object variable always start with self.
        #  while for class we use the name of the class.
        #  in this example Robot.population

    def rise(self):
        if Robot.population > 0:
            print("My name is {} and my kind are {}\
                    in this planet".format(self.name, Robot.population))
        else:
            print("Robots have retired to their galaxy")


p = Robot(input("what will you name ur robot? "))
p.rise()
