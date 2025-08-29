#!/usr/bin/python3

"""
Write a function that returns an object
(Python data structure) represented by a JSON string:

Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON
string doesn’t represent an object.
"""


import json


def from_json_string(my_str):
    """
    function for returning the obj in json
    """
    my_str = json.loads(my_str)
    return (my_str)
