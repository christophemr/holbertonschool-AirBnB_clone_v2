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

    def test_city_id(self):
        """init test method """
        new = self.value(city_id='1234-5678', user_id='abcd-efgh', name='Test Place', description='A place for testing',
                         number_rooms=3, number_bathrooms=2, max_guest=4, price_by_night=100, latitude=0.0, longitude=0.0)
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.city_id), expected_type)

    def test_name(self):
        """test name method """
        new = self.value(name='Test Name')
        self.assertEqual(type(new.name), str)


    def test_description(self):
        """Description test method."""
        # Ensure a description is provided to the instance
        new = self.value(description='Test Description')
        self.assertEqual(type(new.description), str)


    def test_number_rooms(self):
        """Testing place number of rooms attribute."""
        new = self.value(number_rooms=3)
        self.assertEqual(type(new.number_rooms), int)


    def test_number_bathrooms(self):
        """test place number of bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """ test place max_guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """ test place price/night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """test place latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """ test place longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """test amenity id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
