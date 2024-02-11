#!/usr/bin/python3
"""Defines unittests for FileStorage class.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests instantiation of FileStorage class."""

    def test_strageinsta(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_stragearg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_strageflepth(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_stragedik(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storageint(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests methods FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "googly")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("googly", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_alarg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_firstone(self):
        odel = BaseModel()
        res = User()
        ate = State()
        ace = Place()
        ty = City()
        nity = Amenity()
        vew = Review()
        models.storage.new(odel)
        models.storage.new(res)
        models.storage.new(ate)
        models.storage.new(ace)
        models.storage.new(ty)
        models.storage.new(nity)
        models.storage.new(vew)
        self.assertIn("BaseModel." + odel.id, models.storage.all().keys())
        self.assertIn(odel, models.storage.all().values())
        self.assertIn("User." + res.id, models.storage.all().keys())
        self.assertIn(res, models.storage.all().values())
        self.assertIn("State." + ate.id, models.storage.all().keys())
        self.assertIn(ate, models.storage.all().values())
        self.assertIn("Place." + ace.id, models.storage.all().keys())
        self.assertIn(ace, models.storage.all().values())
        self.assertIn("City." + ty.id, models.storage.all().keys())
        self.assertIn(ty, models.storage.all().values())
        self.assertIn("Amenity." + nity.id, models.storage.all().keys())
        self.assertIn(nity, models.storage.all().values())
        self.assertIn("Review." + vew.id, models.storage.all().keys())
        self.assertIn(vew, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
