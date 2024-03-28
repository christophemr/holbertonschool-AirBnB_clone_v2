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
