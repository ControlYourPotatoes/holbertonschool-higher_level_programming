#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Class rectangle that defines a rectangel"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor Method for Rectangle """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Private instnace attributte: width  """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instnace attributte: height  """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the Rectangle Area """

        return self.__width * self.__height

    def perimeter(self):
        """Returns the Rectangle Perimeter"""

        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.__width is 0 or self.__height is 0:
            return ""
        string_rep = ""
        for i in range(self.__height):
            string_rep += str(self.print_symbol) * self.__width
            if i is not self.__height - 1:
                string_rep += "\n"
        return string_rep

    def __repr__(self):
        """return a string representation of
        the rectangle to be able to recreate
        a new instance by"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""

        print("Bye rectangle...")

    def __del__(self):
        """Attribute Decremented during
         each instance deletion"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
