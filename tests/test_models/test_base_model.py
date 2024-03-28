#!/usr/bin/python3
"""BaseModel tests."""
from models.base_model import BaseModel, Base
import unittest
from datetime import datetime  # Ensure this import is correct
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """BaseModel test class"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel test class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up method"""
        pass

    def tearDown(self):
        """Teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the BaseModel class."""
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """Default test."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """BaseModel test with kwargs."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """BaseModel test with int kwargs."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """str method test."""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(
            self.name, i.id, i.__dict__))

    def test_todict(self):
        """test to_dict method."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """kwargs test with none."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """kwargs test with one."""
        n = {'Name': 'test'}
        # Assuming this is expected to work or fail in a specific way
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ID test of model."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """created at test."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """updated at test."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()
