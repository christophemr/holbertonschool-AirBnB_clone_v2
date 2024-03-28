#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage class."""

    def setUp(self):
        """Set up for the tests."""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up tasks."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_save(self):
        """Test saving objects to file."""
        base_model_instance = BaseModel()
        self.storage.new(base_model_instance)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test loading objects from file."""
        base_model_instance = BaseModel()
        self.storage.new(base_model_instance)
        self.storage.save()

        # Create a new storage instance to test reloading
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn(f"BaseModel.{base_model_instance.id}", objects.keys())

    def test_all(self):
        """Test that all returns all stored objects."""
        initial_count = len(self.storage.all())
        new_object = BaseModel()
        self.storage.new(new_object)
        self.storage.save()
        self.assertEqual(len(self.storage.all()), initial_count + 1)

    def test_new(self):
        """Test that new adds an object to the storage."""
        new_object = BaseModel()
        self.storage.new(new_object)
        self.assertIn(f"BaseModel.{new_object.id}", self.storage.all())


if __name__ == '__main__':
    unittest.main()
