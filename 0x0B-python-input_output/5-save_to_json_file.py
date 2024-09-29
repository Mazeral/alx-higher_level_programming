#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj (any): The Python object to serialize and write to the file.
        filename (str): The name of the file where the JSON representation will
        be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
