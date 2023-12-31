#!/usr/bin/python3
""" This module contains class Student """


class Student:
    """ Declaration of class Students """
    def __init__(self, first_name, last_name, age):
        """ Initialize the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Dictionary representation
        of the Student class
        """
        return self.__dict__
