#!/usr/bin/python3
"""This module serializes and deserializes json file"""
import json
from os.path import exists


class FileStorage():
    """Serializes instances to a Json file and
    deserializes Json file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj with the key <obj class name>.id
        in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = FileStorage.__objects
        output = {k: v.to_dict() for k, v in obj_dict.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(output, f, sort_keys=True, indent=4)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except Exception:
            pass
