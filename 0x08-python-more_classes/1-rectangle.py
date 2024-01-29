#!/usr/bin/python3
"""Rectangle class

Rectangle class with some defined attributes.
"""


class Rectangle:
    """Rectangle class the basic backbone of a class
    """
    def __init__(self, width):
        self.__width = width

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

