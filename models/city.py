#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
        City inherits from BaseModel and Base (respect the order)
        class attribute __tablename__ :
        represents the table name, cities
        class attribute name :
        represents a column containing a string (128 characters)
        can’t be null
        class attribute state_id :
        represents a column containing a string (60 characters)
        can’t be null,
        is a foreign key to states.id
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
