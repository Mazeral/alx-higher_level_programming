#!/usr/bin/python3
"""
Rectangle class with some defined attributes.
"""


class Rectangle:
    """Rectangle class the basic backbone of a class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
