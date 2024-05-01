#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a new rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ''
        out = ''
        for i in range(self.__height):
            for _ in range(self.__width):
                out += '#'
            out += '\n' if i != self.__height - 1 else ""
        return out

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)
