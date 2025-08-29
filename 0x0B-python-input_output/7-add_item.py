#!/usr/bin/python3

"""
Write a script that adds all arguments
to a Python list, and then save them to a file:

You must use your function save_to_json_file
from 5-save_to_json_file.py
You must use your function load_from_json_file
from 6-load_from_json_file.py
The list must be saved as a JSON
representation in a file named add_item.json
If the file doesn’t exist, it should be created
"""


import sys  # will be used for arguments couting
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items_list = load_from_json_file(filename)
except:
    items_list = []

items_list = items_list + sys.argv[1:]

save_to_json_file(items_list, "add_item.json")
