#!/usr/bin/python3
"""Defines unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def setUp(self):
        """Sets up shared testing variables."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Tests id attribute."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(-1)
        self.assertEqual(b4.id, -1)

    def test_to_json_string(self):
        """Tests to_json_string method."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), "[{\"id\": 1}]")

    def test_from_json_string(self):
        """Tests from_json_string method."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{\"id\": 1}]"), [{"id": 1}])

    def test_create(self):
        """Tests create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)