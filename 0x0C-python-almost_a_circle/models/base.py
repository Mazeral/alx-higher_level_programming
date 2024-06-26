#!/usr/bin/python3
"""The base class for the rest of the project"""
import json


class Base:
    """Class base

    Attributes:
        id: The identifier of the object
    """
    id = 0

    __nb_objects = 0

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
            Base.__nb_objects = Base.__nb_objects + 1
        else:
            self.id = self.__nb_objects + 1
            Base.__nb_objects = Base.__nb_objects + 1

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            cls.__name__ = "Rectangle":
                new cls(1, 1)
            else:
                new cls(1)
            new.update(**dictionary)
            return new

    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
