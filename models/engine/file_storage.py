#!/usr/bin/python3
"""FileStorage module for AirBnB clone"""

import json
from models.base_model import BaseModel
from models.state import State
from models.place import Place

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def delete(self, obj=None):
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]
