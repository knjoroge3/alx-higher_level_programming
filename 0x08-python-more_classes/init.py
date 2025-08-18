#!/usr/bin/python3


"""
This program explains the __init__ method
"""

class MyClass:
    def __init__(self, name):  # A special method in python that is run after the an object is created and normally used to set variables
        self.name = name  #  here there are a few things going on
        #  the first self.name is an instance variable
        #  the second name is the argument (2nd one in logic but 1st in python after self) passed after the init method

    def say_hi(self):  # the defining of the say_hi method
        print("Hello Mr.{}, welcome to github".format(self.name))  # what the method will do

p = MyClass('Talam')
p.say_hi()
