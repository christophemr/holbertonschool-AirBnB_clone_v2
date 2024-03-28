#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv
import models

# Association table for the many-to-many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """A place to stay"""
    id = Column(String(60), primary_key=True)
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # Relationships
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != 'db':
        @property
        def reviews(self):
            """File storage relationship simulation for reviews."""
            review_list = []
            for review in list(all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """File storage getter for amenities."""
            amenities = []
            for amenity in list(all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """File storage setter for amenities."""
            if type(value).__name__ == 'Amenity':
                self.amenity_ids.append(value.id)
