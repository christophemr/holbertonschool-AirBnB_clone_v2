#!/usr/bin/python3
"""Unit tests for the Place class."""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os
import unittest


class test_Place(test_basemodel):
    """Define unit tests for the Place class."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def setUp(self):
        """Set up for the tests."""
        self.new = self.value()

    def test_attributes_exist(self):
        """Test that Place attributes exist."""
        attributes = [
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ]
        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.new, attr), f"{attr} is missing")

    def test_attributes_type(self):
        """Test Place attributes have the correct type."""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            if self.new.user_id is not None:
                self.assertIsInstance(
                    self.new.user_id, str, "user_id is not a string")
            if self.new.name is not None:
                self.assertIsInstance(self.new.name, str,
                                      "name is not a string")
            if self.new.description is not None:
                self.assertIsInstance(
                    self.new.description, str, "description is not a string")
            if self.new.number_rooms is not None:
                self.assertIsInstance(
                    self.new.number_rooms, int, "number_rooms is not an int")
            if self.new.number_bathrooms is not None:
                self.assertIsInstance(
                    self.new.number_bathrooms, int, "number_bathrooms is not an int")
            if self.new.max_guest is not None:
                self.assertIsInstance(self.new.max_guest,
                                      int, "max_guest is not an int")
            if self.new.price_by_night is not None:
                self.assertIsInstance(
                    self.new.price_by_night, int, "price_by_night is not an int")
            if self.new.latitude is not None:
                self.assertIsInstance(
                    self.new.latitude, float, "latitude is not a float")
            if self.new.longitude is not None:
                self.assertIsInstance(self.new.longitude,
                                      float, "longitude is not a float")
            if self.new.amenity_ids is not None:
                self.assertIsInstance(
                    self.new.amenity_ids, list, "amenity_ids is not a list")
