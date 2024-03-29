#!/usr/bin/python3
""" State Module for HBNB project """
from models.amenity import Amenity  # Import Amenity class
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import unittest


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_name2(self):
        """Test that name attribute is of type str"""
        new = Amenity(
            name="Test Amenity")
        self.assertIsInstance(new.name, str)
