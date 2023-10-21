#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
