#!/usr/bin/python3
"""Defines unittests for amenity class.

Unittest classes:
    TestAmenity_instantiation
"""
import unitests
import models
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests instantiation of the Amenity class."""

    def test_zeroargs(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_storenewobj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_upddate(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_isname(self):
        nity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", nity.__dict__)

    def test_twnitys(self):
        nity1 = Amenity()
        nity2 = Amenity()
        self.assertNotEqual(nity1.id, nity2.id)


if __name__ == "__main__":
    unittest.main()
