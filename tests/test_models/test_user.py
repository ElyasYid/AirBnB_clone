#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
"""
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests instantiation of User class."""

    def test_noinput(self):
        self.assertEqual(User, type(User()))

    def test_neisnta(self):
        self.assertIn(User(), models.storage.all().values())

    def test_idchcece(self):
        self.assertEqual(str, type(User().id))

    def test_createchecko(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updateckk(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_emaipubstr(self):
        self.assertEqual(str, type(User.email))

    def test_passwopub(self):
        self.assertEqual(str, type(User.password))

    def test_finame(self):
        self.assertEqual(str, type(User.first_name))

    def test_laname(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        ree1 = User()
        ree2 = User()
        self.assertNotEqual(ree1.id, ree2.id)


if __name__ == "__main__":
    unittest.main()
