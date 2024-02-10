#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_stan
    TestBaseModel_save
    TestBaseModel_tod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
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


class TestBaseModel_save(unittest.TestCase):
    """Unittests save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_fvse(self):
        wert = BaseModel()
        sleep(1)
        first_updated_at = wert.updated_at
        wert.save()
        self.assertLess(first_updated_at, wert.updated_at)

    def test_nvra2(self):
        wert = BaseModel()
        sleep(1)
        first_updated_at = wert.updated_at
        wert.save()
        second_updated_at = wert.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(1)
        wert.save()
        self.assertLess(second_updated_at, wert.updated_at)

    def test_opasdn(self):
        wert = BaseModel()
        with self.assertRaises(TypeError):
            wert.save(None)

    def test_inbvx(self):
        wert = BaseModel()
        wert.save()
        wertid = "BaseModel." + wert.id
        with open("file.json", "r") as f:
            self.assertIn(wertid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests to_dict method of the BaseModel class."""

    def test_bvnryw(self):
        wert = BaseModel()
        self.assertTrue(dict, type(wert.to_dict()))

    def test_jhvasdz(self):
        wert = BaseModel()
        self.assertIn("id", wert.to_dict())
        self.assertIn("created_at", wert.to_dict())
        self.assertIn("updated_at", wert.to_dict())
        self.assertIn("__class__", wert.to_dict())

    def test_namia(self):
        wert = BaseModel()
        wert.name = "Bobby"
        wert.my_number = 67
        self.assertIn("name", wert.to_dict())
        self.assertIn("my_number", wert.to_dict())

    def test_opla(self):
        wert = BaseModel()
        wert_dict = wert.to_dict()
        self.assertEqual(str, type(wert_dict["created_at"]))
        self.assertEqual(str, type(wert_dict["updated_at"]))

    def test_gonder(self):
        dt = datetime.today()
        wert = BaseModel()
        wert.id = "78900"
        wert.created_at = wert.updated_at = dt
        tdict = {
            'id': '78900',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(wert.to_dict(), tdict)

    def test_lalibela(self):
        wert = BaseModel()
        self.assertNotEqual(wert.to_dict(), wert.__dict__)

    def test_axum(self):
        wert = BaseModel()
        with self.assertRaises(TypeError):
            wert.to_dict(None)


if __name__ == "__main__":
    unittest.main()
