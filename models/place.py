#!/usr/bin/python3
"""Place Module for HBNB project"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
# Assuming Amenity is correctly imported
from models.amenity import Amenity

# Many-to-many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    # Existing columns
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
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, back_populates="place_amenities")

    amenity_ids = []  # Needed for FileStorage

    @property
    def reviews(self):
        """FileStorage relationship between Place and Review."""
        from models import storage
        all_reviews = storage.all(Review)
        place_reviews = [
            review for review in all_reviews.values() if review.place_id == self.id]
        return place_reviews

    @property
    def amenities(self):
        """Getter for amenities, FileStorage mode."""
        from models import storage
        return [storage.all(Amenity).get('Amenity.' + id_) for id_ in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """Setter for amenities, FileStorage mode."""
        if not isinstance(obj, Amenity):
            return
        self.amenity_ids.append(obj.id)
