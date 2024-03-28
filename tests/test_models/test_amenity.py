#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os


class test_Amenity(test_basemodel):
    """amenity test class """

    def __init__(self, *args, **kwargs):
        """init test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

