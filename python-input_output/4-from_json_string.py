#!/usr/bin/python3
"""This module contains function from_json_string"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """
    return json.loads(my_obj)
