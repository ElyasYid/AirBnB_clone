#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj"""
        obj_cls_nm = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_nm, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        od = FileStorage.__objects
        o_dict = {obj: od[obj].to_dict() for obj in od.keys()}
        with open(FileStorage.__file_path, "w") as d:
            json.dump(o_dict, d)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects"""
        try:
            with open(FileStorage.__file_path) as d:
                o_dict = json.load(d)
                for o in o_dict.values():
                    cls_n = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_n)(**o))
        except FileNotFoundError:
            return
