#!/usr/bin/python3
"""
This module contains that compares a class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly) from a_class.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
