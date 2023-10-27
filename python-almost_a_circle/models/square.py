#!/usr/bin/python3
"""Square Class Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override __str__ with new string in the format"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
