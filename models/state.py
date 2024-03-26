#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """FileStorage relationship between State and City"""
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
