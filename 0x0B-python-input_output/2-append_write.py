#!/usr/bin/python3

"""
Write a function that appends a
string at the end of a text file
(UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_write(filename="", text=""):
    """
    appends information to a file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
