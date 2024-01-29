#!/usr/bin/python3
"""
Rectangle class with some defined attributes.
"""


class Rectangle:
    """Rectangle class the basic backbone of a class
    """
    def __init__(self, width=0, height=0):
        """The __init__ of the object

            Args:
                self (obj): the object itself
                width (int): The width of the Rectangle
                height (int): The height of the Rectangle
            
            Returns: Nothing

            Raises:
                TypeError: if width or height is not an integer
                ValueError: if width or height is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            return TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            return TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
