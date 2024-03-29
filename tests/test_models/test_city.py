#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """ tests for city class"""

    def __init__(self, *args, **kwargs):
        """init the test class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute"""
        new = City()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertIsNone(new.state_id)
        else:
            self.assertIsInstance(new.state_id, str)


    def test_name(self):
        """Test name attribute"""
        new = City()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
                self.assertIsNone(new.name)
        else:
            self.assertIsInstance(new.name, str)
