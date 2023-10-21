#!/usr/bin/python3
"""This module contains function from_json_string"""


import json


def to_json_string(my_obj):
    """
    This function returns an objects
    represented by a JSON string
    """
    return json.loads(my_obj)
