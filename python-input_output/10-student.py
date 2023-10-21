#!/usr/bin/python3
""" This module contains class Student """


class Student:
    """
    A class Student that defines a student by
    some public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given 
        first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
