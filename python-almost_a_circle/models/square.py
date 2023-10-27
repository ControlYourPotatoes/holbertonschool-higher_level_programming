#!/usr/bin/python3
"""Square Class Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets private instance attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets private instance attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """override __str__ with new string representation"""
        str_rep = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_rep)
    
    def update(self, *args, **kwargs):
        """Assigns the attribute"""
        if args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.width = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1

        for key, elem in kwargs.items():
            if key == "id":
                self.id = elem
            if key == "size":
                self.width = elem
            if key == "x":
                self.x = elem
            if key == "y":
                self.y = elem
