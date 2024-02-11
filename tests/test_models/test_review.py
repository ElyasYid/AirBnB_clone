#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
"""
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests instantiation of the Review class."""

    def test_zeroinput(self):
        self.assertEqual(Review, type(Review()))

    def test_newins(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_strid(self):
        self.assertEqual(str, type(Review().id))

    def test_createcheck(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updatecheck(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_tworeun(self):
        crit1 = Review()
        crit2 = Review()
        self.assertNotEqual(crit1.id, crit2.id)


if __name__ == "__main__":
    unittest.main()
