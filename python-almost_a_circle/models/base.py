#!/usr/bin/python3
"""Base Class Module"""

import json
from os import path

class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))
