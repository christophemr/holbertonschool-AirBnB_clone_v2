#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
import models


#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True,
                nullable=False) if models.storage_t == 'db' else ''
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow) if models.storage_t == 'db' else datetime.utcnow()
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow) if models.storage_t == 'db' else datetime.utcnow()

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            if key not in ("__class__", "_sa_instance_state"):
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete instance from storage by calling the delete method"""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
            elif key != '_sa_instance_state':
                dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
