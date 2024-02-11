#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
"""
import models
import unittest
from datetime import datetime
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests instantiation of the Place class."""

    def test_zeroinput(self):
        self.assertEqual(Place, type(Place()))

    def test_newinput(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_idcheck(self):
        self.assertEqual(str, type(Place().id))

    def test_creatcheck(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updatecheck(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_twouniq(self):
        area1 = Place()
        area2 = Place()
        self.assertNotEqual(area1.id, area2.id)


if __name__ == "__main__":
    unittest.main()
