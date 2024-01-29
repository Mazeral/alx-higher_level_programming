#!/usr/bin/python3
def add_integer(a, b=98):
    """```add_integer``` adds two numbers, raises TypeError otherwise.

    Args:
        `a`: The first number
        `b`: The second number

    Returns:
        The sum of the two numbers

    Raises:
        ValueError if either a or b are not numbers
    """

    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    return int(a) + int(b)
