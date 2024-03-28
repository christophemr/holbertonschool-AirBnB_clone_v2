#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os


class test_User(test_basemodel):
    """Test user class"""

    def __init__(self, *args, **kwargs):
        """Test user class init"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """Set up for each test method."""
        super().setUp()
        self.user = self.value()
        # Set default attributes for the user, ensuring they are not None if not using 'db' storage
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.user.email = "user@example.com"
            self.user.first_name = "Test"
            self.user.last_name = "User"
            self.user.password = "password"

    def test_first_name(self):
        """User first name test."""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(self.user.first_name),
                         expected_type, "First name type mismatch")

    def test_last_name(self):
        """User last name test."""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(self.user.last_name),
                         expected_type, "Last name type mismatch")

    def test_email(self):
        """User email test."""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(self.user.email),
                         expected_type, "Email type mismatch")

    def test_password(self):
        """User password test."""
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(self.user.password),
                         expected_type, "Password type mismatch")
