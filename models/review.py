#!/usr/bin/python3
"""Review module for the HBNB project"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    id = Column(String(60), primary_key=True)
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
