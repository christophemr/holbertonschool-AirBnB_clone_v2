#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """test state class """

    def __init__(self, name):
        """ test state class init"""
        self.id = id(self)
        self.name = name
