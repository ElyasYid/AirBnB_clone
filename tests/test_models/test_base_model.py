#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

    Unittest classes:
        TestBaseModel_stan
"""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittest for instantiation of the BaseModel class."""

    def test_ajnk(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_oibef(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_rtua(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_polaaw(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_nvrfjal(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))


if __name__ == "__main__":
    unittest.main()
