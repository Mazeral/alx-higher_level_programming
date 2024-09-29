#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a UTF-8 encoded file and prints its content.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
