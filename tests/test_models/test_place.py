#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ test place class"""

    def __init__(self, *args, **kwargs):
        """init tests class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def setUp(self):
        """Set up for the tests"""
        self.new = self.value()

    def test_city_id(self):
        """init test method """
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.city_id, expected_type))

    def test_user_id(self):
        """ user test method"""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.user_id, expected_type))

    def test_name(self):
        """test name method """
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.name, expected_type))

    def test_description(self):
        """ description test method"""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.description, expected_type))

    def test_number_rooms(self):
        """testing place number of rooms attr"""
        expected_type = int if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.number_rooms, expected_type))

    def test_number_bathrooms(self):
        """test place number of bathrooms """
        expected_type = int if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.number_bathrooms, expected_type))

    def test_max_guest(self):
        """ test place max_guest"""
        expected_type = int if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.max_guest, expected_type))

    def test_price_by_night(self):
        """ test place price/night"""
        expected_type = int if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.price_by_night, expected_type))

    def test_latitude(self):
        """test place latitude """
        expected_type = float if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.latitude, expected_type))

    def test_longitude(self):
        """ test place longitude"""
        expected_type = float if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.longitude, expected_type))

    def test_amenity_ids(self):
        """test amenity id """
        expected_type = list if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertTrue(isinstance(self.new.amenity_ids, expected_type))
