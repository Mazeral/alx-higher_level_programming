#!/usr/bin/python3
"""
Square class

A class which defines a class which computes some of the square properties.

"""


class Square():
    """An empty Square class"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            print("size must be an integer", end='')
            raise TypeError
        if size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size

        # The position definition part
        if not (isinstance(position[0], int) and isinstance(position[1], int)
                and position[0] >= 0 and position[1] >= 0):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer", end='')
            raise TypeError
        if size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size

    @property
    def position(self):
        """The position property."""
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print("")
