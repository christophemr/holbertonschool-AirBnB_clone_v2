#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """review test class """

    def __init__(self, *args, **kwargs):
        """ review class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test review place_id """
        # Assuming 'valid_place_id' is a valid place_id for testing purposes
        valid_place_id = "valid_place_id"
        new = self.value(place_id=valid_place_id)
        self.assertEqual(type(new.place_id), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))

    def test_user_id(self):
        """review user_id test """
        # Assuming 'valid_user_id' is a valid user_id for testing purposes
        valid_user_id = "valid_user_id"
        new = self.value(user_id=valid_user_id)
        self.assertEqual(type(new.user_id), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))


    def test_text(self):
        """review text test """
        # Assuming 'valid_text' is a valid text for testing purposes
        valid_text = "This is a valid review text."
        new = self.value(text=valid_text)
        self.assertEqual(type(new.text), str if
                        os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                        type(None))
