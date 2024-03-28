#!/usr/bin/python3
"""This module instantiates an object
    of class FileStorage
    if the environmental variable is set to "db",
    instantiates a dbstorage
    otherwise, instantiates FileStorage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
