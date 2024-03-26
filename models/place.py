#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False, backref="place_amenities")
    else:
        @property
        def amenities(self):
            """FileStorage relationship between Place and Amenity"""
            from models import storage
            from models.amenity import Amenity
            all_amenities = storage.all(Amenity)
            return [amenity for amenity in all_amenities.values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
