#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
import models
from os import getenv


# Conditional base declaration based on the storage type
Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                # Convert string timestamps to datetime objects
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            if key != "__class__":
                setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__ of the instance.
        This includes the class name, and the created_at and updated_at times
        formatted as strings. It also handles removing any SQLAlchemy specific
        attributes.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()

        # Exclude SQLAlchemy's instance state attribute, if present
        dict_repr.pop("_sa_instance_state", None)

        return dict_repr

    @classmethod
    def prepare(cls, engine):
        """
        Prepares the class for use with SQLAlchemy, if database storage is used.
        This method is only relevant when transitioning from file to DB storage.
        """
        if getenv("HBNB_TYPE_STORAGE") != 'db':
            cls.__table__.create(bind=engine, checkfirst=True)
