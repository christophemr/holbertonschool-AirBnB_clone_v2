from unittest import TestCase
from models.state import State
import os


class test_state(TestCase):
    """Test the State class"""

    def test_name3(self):
        """Test that the 'name' attribute of a State instance is correctly typed."""
        new = State()
        expected_type = str if os.getenv(
            'HBNB_TYPE_STORAGE') != 'db' else type(None)
        new.name = "Test State"
        self.assertIsInstance(new.name, expected_type, f"The 'name' attribute is expected to be of type {
                              expected_type}, but got {type(new.name)}")
