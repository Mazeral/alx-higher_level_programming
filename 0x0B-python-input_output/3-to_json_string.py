#!/usr/bin/python3
"""a function that returns the JSON representation of an object (string)"""


import json


def to_json_string(obj):
    """
    Returns the JSON representation of an object (Python data structure).

    Args:
        obj (any): The Python object to serialize.

    Returns:
        str: A JSON string representation of the object.
    """
    return json.dumps(obj)
