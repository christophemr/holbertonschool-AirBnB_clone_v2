import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for other models."""
    if models.storage_t == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, **kwargs):
        """Initializes the base model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            kwargs.setdefault('id', str(uuid.uuid4()))
            kwargs.setdefault('created_at', datetime.utcnow())
            kwargs.setdefault('updated_at', datetime.utcnow())
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at'] and isinstance(value, str):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def save(self):
        """Updates 'updated_at' with the current datetime and saves the model."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage."""
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

    def delete(self):
        """
            Delete current instance from storage by calling its delete method
        """
        from models import storage
        storage.delete(self)
