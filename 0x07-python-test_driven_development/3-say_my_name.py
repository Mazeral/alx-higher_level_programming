#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """`say_my_name` prints: ``My name is <first_name> <last_name>``

        Args:
            `first_name`: A string, must exist.
            `last_name`: A string, with default value of `""`

        Returns
            Nothing really.

        Raises:
            ValueError if one of the `Args` is not a string.
        """
    if not isinstance(first_name, str):
        raise ValueError("first_name must be a name")
    if not isinstance(last_name, str):
        raise ValueError("last_name must be a name")
    print("My name is {} {}".format(first_name, last_name))
