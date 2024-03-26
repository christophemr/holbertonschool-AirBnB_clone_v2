#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

data_storage_type = os.getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """Representation of city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if data_storage_type == 'db':
        state = relationship("State", back_populates="cities")
        places = relationship("Place", backref="cities",
                              cascade="delete-orphan")

    else:
        name = ""
        state_id = ""
