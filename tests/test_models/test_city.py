#!/usr/bin/python3
"""Defines unittests for models/city.py.

    Unittest classes:
        TestCity_instantiation
"""
import models
import unittest
from datetime import datetime
from models.city import City


class TestCity_instatiation(unittest.TestCase):
    """Unittests instantiation of the City class."""

    def test_zeroinput(self):
        self.assertEqual(City, type(City()))

    def test_newinsta(self):
        self.assertIn(City(), models.storage.all().values())

    def test_iips(self):
        self.assertEqual(str, type(City().id))

    def test_creaipd(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updipd(self):
        self.assertEqual(datetime, type(City().updated_at))


if __name__ == "__main__":
    unittest.main()
