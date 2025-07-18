#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        last = (number % 10)
        print("{}".format(last), end="")
    elif number < 0:
        number *= -1
        last = (number % 10)
        print("{}".format(last), end="")
    return last
