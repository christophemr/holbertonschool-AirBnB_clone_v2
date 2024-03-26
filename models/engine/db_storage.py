#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
import models
from os import getenv

# Conditionally create the Base class for SQLAlchemy or a dummy object
Base = declarative_base() if getenv("HBNB_TYPE_STORAGE") == 'db' else object


class BaseModel:
    """A base class for all hbnb models"""
    # Define columns if in DB storage mode
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.utcnow()

        for key, value in kwargs.items():
            if key not in ("__class__", "_sa_instance_state"):
                if key in ("created_at", "updated_at") and isinstance(value, str):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls_name = type(self).__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat() if isinstance(
            self.created_at, datetime) else self.created_at
        dictionary['updated_at'] = self.updated_at.isoformat() if isinstance(
            self.updated_at, datetime) else self.updated_at
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Delete instance from storage by calling the delete method"""
        models.storage.delete(self)
