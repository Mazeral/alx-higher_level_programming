#!/usr/bin/python3
"""
Square class

A class which defines a class which computes some of the square properties.

"""


class Square():
    """An empty Square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            print("size must be an integer", end='')
            raise TypeError
        if size < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = size

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

    def my_print(self):
        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end='')
            print("")
