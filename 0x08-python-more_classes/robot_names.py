#!/usr/bin/python3

"""
This code shows how you can use attributes
using the . notation to create members of a
class
"""


class RobotName:
    pass


x = RobotName()
y = RobotName()
x.name = "Miller"
x.build_year = "1967"
y.name = "BT"
y.build_year = "2024"


print("{} and was built on {}".format(x.name, x.build_year))
print("{} and was built on {}".format(y.name, y.build_year))
