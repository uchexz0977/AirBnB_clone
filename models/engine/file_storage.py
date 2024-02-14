#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the object storage."""
        class_name = obj.__class__.__name__
        obj_key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serialize the object storage to a JSON file."""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialize the JSON file to populate the object storage."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    del val['__class__']
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            pass

