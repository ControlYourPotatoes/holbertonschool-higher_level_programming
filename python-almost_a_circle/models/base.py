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

    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as fd:
            list_instance = []
            if list_objs is None:
                fd.write(cls.to_json_string(list_instance))
            else:
                for i in list_objs:
                    list_instance.append(i.to_dictionary())
                fd.write(cls.to_json_string(list_instance))
