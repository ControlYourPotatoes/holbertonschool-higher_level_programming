#!/usr/bin/python3
"""This module has function named append_write"""


def append_write(filename="", text=""):
    """Append write to a file"""
    with open(filename, 'a') as fd:
        return fd.write(text)
