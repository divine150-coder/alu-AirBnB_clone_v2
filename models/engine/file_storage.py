#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.state import State
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "State": State,
    "Place": Place
}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for k, v in objs.items():
                cls_name = v["__class__"]
                self.new(classes[cls_name](**v))
        except FileNotFoundError:
            pass
