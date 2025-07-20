#!/usr/bin/python3

import sys

# Write a program that prints the result of the addition of all arguments

if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0
    for i in args:
        total += int(i)
    print("{}".format(total))
