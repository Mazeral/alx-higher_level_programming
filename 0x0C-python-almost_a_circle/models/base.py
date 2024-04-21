#!/usr/bin/python3
"""The base class for the rest of the project"""

class Base:
    """Class base

    Attributes:
        id: The identifier of the object
    """
    id = 0
    def __init__(self, id=None):
        """The __init__ of the __nb_objects

        Args:
            self: Class attributes reference
            id: The indentifer of the object

        Returns: Nothing

        Raises: Nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.id = Base.id + 1

