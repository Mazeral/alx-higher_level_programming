#!/usr/bin/python3
"""
Rectangle class with some defined attributes.
"""


class Rectangle:
    """
    Rectangle class the basic backbone of a class

    Attributes:
        width (int, optional): the width of the Rectangle
        height(int, optional): the height of the Rectangle
    """
    def __init__(self, width=0, height=0):
        """The __init__ of the object

            Args:
                self (obj): the object itself
                width (int, optional): The width of the Rectangle
                height (int, optional): The height of the Rectangle

            Returns: Nothing

            Raises:
                TypeError: if width or height is not an integer
                ValueError: if width or height is less than 0
        """
        if not isinstance(width, int):
            return TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            return TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        """
        area: returns the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter: returns the perimeter of the rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """creates the rectangle and returns it"""
        rec = []
        if self.__width is 0 or self.__height is 0:
            rec.append("")
            return
        for i in range(self.__height):
            for k in range(self.__width):
                rec.append("#")
            rec.append("\n")
        rec.pop()
        return "".join(rec)
