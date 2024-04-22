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

    def area(self):
        return self.__width * self.__height

    def display(self):
        for vertical_offset in range(self.__y):
            print("")
        for x_display in range(self.__height):
            for horizontal_offset in range(self.__x):
                print(" ", end="")
            for y_display in range(self.__width):
                print('#', end="")
            print("")
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        if len(args) > 0 and args[0]:
            self.id = args[0]
        if len(args) > 1 and args[1]:
            self.__width = args[1]
        if len(args) > 2 and args[2]:
            self.__height = args[2]
        if len(args) > 3 and args[3]:
            self.__x = args[3]
        if len(args) > 4 and args[4]:
            self.__y = args[4]
