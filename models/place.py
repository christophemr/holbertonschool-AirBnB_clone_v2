#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table
from os import getenv
import models

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True)
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
    reviews = relationship("Review", backref="place",
                           cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Getter for file storage to simulate DB relationship."""
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]
        return self._reviews

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
