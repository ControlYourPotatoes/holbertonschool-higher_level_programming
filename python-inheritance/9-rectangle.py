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

    def __str__(self):
        """Return a description of the Rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.__width * self.__height
