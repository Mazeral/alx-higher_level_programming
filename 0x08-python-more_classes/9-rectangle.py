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
        number_of_instances (int): The number of class instances
    """

    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal: returns the intance which have bigger Rectangle size

            Args:
                rect_1: The first Rectangle instance
                rect_2: The second Rectangle instance

            Returns:
                the bigger size Rectangle instance
                if equal, returns rect_1

            Raises:
                TypeError if either of the paramters are NOT Rectangle instnaces
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        """creates the rectangle and returns it"""
        rec = []
        if self.__width == 0 or self.__height == 0:
            rec.append("")
            return
        for i in range(self.__height):
            for k in range(self.__width):
                rec.append(str(self.print_symbol))
            rec.append("\n")
        rec.pop()
        return "".join(rec)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """adding more functionality to del"""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
