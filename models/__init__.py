#!/usr/bin/python3
"""This module instantiates an object
    of class FileStorage
    if the environmental variable is set to "db",
    instantiates a dbstorage
    otherwise, instantiates FileStorage
"""
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
