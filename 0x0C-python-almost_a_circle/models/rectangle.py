#!/usr/bin/python3
from .base import Base

"""Rectange class based on the Base class"""

class Rectangle(Base):
    """docstring for Rectange.

    Attributes:
        __width: The width of the Rectange
        __height: The height of the Rectange
        __x: The horizontal cordination of the Rectange
        __y: The vertical cordination of the Rectange
    """
    def __init__(self, width, height, x = 0, y = 0, id = None):
        """The __init__ of the Rectange class
        
        Args:
            width: Sets the width of the Rectange
            height: sets the height of the Rectange
            x: horizontal cordination
            y: vertical cordination
            id: The id of the object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
