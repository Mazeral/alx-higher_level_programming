#!/usr/bin/python3
"""
Square class

A basic class
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
