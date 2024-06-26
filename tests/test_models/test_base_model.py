#!/usr/bin/python3
""" """
from models.base_model import BaseModel, Base
import unittest
from datetime import datetime
from uuid import UUID
import json
import os
import time
from unittest.mock import patch
from datetime import datetime, timedelta


class test_basemodel(unittest.TestCase):
    """ base_model test class"""

    def __init__(self, *args, **kwargs):
        """init basemodel test class """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up method """
        pass

    def tearDown(self):
        """teardown method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the model class.
        """
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_default(self):
        """default test """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """bm test with kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """bm test with int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Testing save method of BaseModel"""
        i = BaseModel()
        i.save()
        mock_storage.new.assert_called_once_with(i)
        mock_storage.save.assert_called_once()

    def test_str(self):
        """str method test """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test to_dict method  """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ kwargs test with none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """id test of model """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """created at test """
        new = self.value()
        # Changed from datetime.datetime to datetime
        self.assertEqual(type(new.created_at), datetime)

    @patch('models.storage')
    def test_updated_at(self, mock_storage):
        """updated at test """
        # Create a new instance of BaseModel
        new = BaseModel()

        # Set up mock for datetime
        with patch('models.base_model.datetime') as mock_datetime:
            now = datetime.now()
            mock_datetime.now.return_value = now

            # Save the new instance
            new.save()

            # Set future time for updating
            future = now + timedelta(seconds=1)
            mock_datetime.now.return_value = future

            # Save again to trigger updating
            new.save()

            # Assert that updated_at is equal to future time
            self.assertNotEqual(new.created_at, new.updated_at)
            self.assertEqual(new.updated_at, future)
