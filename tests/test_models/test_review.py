#!/usr/bin/python3
import unittest
import os
from models.review import Review
from tests.test_models.test_base_model import test_basemodel


class test_review(test_basemodel):
    """Review test class"""

    def __init__(self, *args, **kwargs):
        """Review class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def setUp(self):
        """Set up for the tests."""
        super().setUp()
        self.model = Review()
        self.model.place_id = "test_place_id"
        self.model.user_id = "test_user_id"
        self.model.text = "test_text"

    def test_place_id_attr(self):
        """Test that Review has attribute place_id and it's as expected."""
        self.assertEqual(self.model.place_id, "test_place_id")

    def test_user_id_attr(self):
        """Test that Review has attribute user_id and it's as expected."""
        self.assertEqual(self.model.user_id, "test_user_id")

    def test_text_attr(self):
        """Test that Review has attribute text and it's as expected."""
        self.assertEqual(self.model.text, "test_text")

    def test_attributes_types(self):
        """Test that Review attributes are of correct type."""
        self.assertIsInstance(self.model.place_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.text, str)



if __name__ == "__main__":
    unittest.main()
