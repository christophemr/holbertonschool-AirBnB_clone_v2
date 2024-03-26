#!/usr/bin/python3
"""This module instantiates an object
    of class FileStorage
    if the environmental variable is set to "db",
    instantiates a dbstorage
    otherwise, instantiates FileStorage
"""
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
