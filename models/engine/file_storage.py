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
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If cls is provided, returns a dictionary of objects of type cls.
        """
        if cls is not None:
            return {key: obj for key, obj in FileStorage.__objects.items()
                    if isinstance(obj, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside.
        If obj is equal to None, the method should not do anything.
        """
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for obj_id, obj_dict in objects.items():
                cls_name = obj_dict['__class__']
                if cls_name in globals():
                    self.__objects[obj_id] = globals()[cls_name](**obj_dict)
        except FileNotFoundError:
            pass
