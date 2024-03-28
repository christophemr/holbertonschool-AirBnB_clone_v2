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
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.new.place_id = "test_place_id"
            self.new.user_id = "test_user_id"
            self.new.text = "test_text"
