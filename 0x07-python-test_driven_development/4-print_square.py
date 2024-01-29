#!/usr/bin/python3
def print_square(size):
    """`print_square`: Prints a square

    Args:
        `size`: The size width and length of the square

    Returns:
        Nothing

    Raises:
        ValueError if the value less than 0
        TypeError if the value is not string
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#", end='')
        print("")
