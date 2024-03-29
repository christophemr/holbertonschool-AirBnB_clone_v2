from unittest import TestCase
from models.state import State
import os


class test_state(TestCase):
    """Test the State class"""

    def test_name3(self):
        """Test that the 'name' attribute of a State instance is correctly typed."""
        new = State()
        new.name = "Test State"
        # The expectation is now that new.name is always a string, regardless of storage type
        self.assertIsInstance(
            new.name, str, "The 'name' attribute is expected to be of type 'str'")
