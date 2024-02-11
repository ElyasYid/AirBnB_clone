#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
"""
import models
import unittest
from datetime import datetime
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests instantiation of State class."""

    def test_zweoinput(self):
        self.assertEqual(State, type(State()))

    def test_newisn(self):
        self.assertIn(State(), models.storage.all().values())

    def test_idcheckk(self):
        self.assertEqual(str, type(State().id))

    def test_creatcheck(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updatcheck(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_unique_ids(self):
        regi1 = State()
        regi2 = State()
        self.assertNotEqual(regi1.id, regi2.id)


if __name__ == "__main__":
    unittest.main()
