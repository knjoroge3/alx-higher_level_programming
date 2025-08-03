#!/usr/bin/python3

class robot:
    pass

if __name__ == "__main__":
    y = robot()
    x = robot()
    x.name = "Marvin"
    x.buildyear = "1979"
    y.name  = "caliban"
    y.buildyear = "1973"

    print("{} = {} \n{} = {}".format(x.name, x.buildyear, y.name, y.buildyear))
