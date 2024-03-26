#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if cls:
            cls_name = cls if isinstance(cls, str) else cls.__name__
            return {k: v for k, v in self.__objects.items() if cls_name in k}
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def delete(self, obj=None):
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                cls_name = obj_data['__class__']
                if cls_name in globals():
                    self.__objects[obj_id] = globals()[cls_name](**obj_data)
        except FileNotFoundError:
            pass
