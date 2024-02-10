#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_nst
    TestCity_save
    TestCity_tod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_nst(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_nai(self):
        self.assertEqual(City, type(City()))

    def test_nisio(self):
        self.assertIn(City(), models.storage.all().values())

    def test_iips(self):
        self.assertEqual(str, type(City().id))

    def test_caipd(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_uaipd(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_au(self):
        kol = City(None)
        self.assertNotIn(None, kol.__dict__.values())


class TestCity_save(unittest.TestCase):
    """Unittests to test save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "kick")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("kick", "file.json")
        except IOError:
            pass

    def test_ons(self):
        kol = City()
        sleep(0.05)
        first_updated_at = kol.updated_at
        kol.save()
        self.assertLess(first_updated_at, kol.updated_at)

    def test_tws(self):
        kol = City()
        sleep(0.05)
        first_updated_at = kol.updated_at
        kol.save()
        second_updated_at = kol.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        kol.save()
        self.assertLess(second_updated_at, kol.updated_at)

    def test_swa(self):
        kol = City()
        with self.assertRaises(TypeError):
            kol.save(None)

    def test_suf(self):
        kol = City()
        kol.save()
        kolid = "City." + kol.id
        with open("file.json", "r") as f:
            self.assertIn(kolid, f.read())


class TestCity_tod(unittest.TestCase):
    """Unittests to test to_dict method of the City class."""

    def test_yfy(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_yfvvl(self):
        kol = City()
        self.assertIn("id", kol.to_dict())
        self.assertIn("created_at", kol.to_dict())
        self.assertIn("updated_at", kol.to_dict())
        self.assertIn("__class__", kol.to_dict())

    def test_yfvss(self):
        kol = City()
        kol.middle_name = "Holberton"
        kol.my_number = 98
        self.assertEqual("Holberton", kol.middle_name)
        self.assertIn("my_number", kol.to_dict())

    def test_yffss(self):
        kol = City()
        kol_dict = kol.to_dict()
        self.assertEqual(str, type(kol_dict["id"]))
        self.assertEqual(str, type(kol_dict["created_at"]))
        self.assertEqual(str, type(kol_dict["updated_at"]))

    def test_ilo(self):
        dt = datetime.today()
        kol = City()
        kol.id = "123456"
        kol.created_at = kol.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(kol.to_dict(), tdict)

    def test_tgen(self):
        kol = City()
        self.assertNotEqual(kol.to_dict(), kol.__dict__)

    def test_lokcc(self):
        kol = City()
        with self.assertRaises(TypeError):
            kol.to_dict(None)


if __name__ == "__main__":
    unittest.main()
