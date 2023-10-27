#!/usr/bin/python3
"""Module to test rentangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_width(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height(self):
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_x(self):
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_y(self):
        r = Rectangle(10, 20)
        r.y = 40
        self.assertEqual(r.y, 40)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)

    def test_str(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (50) 30/40 - 10/20")

    def test_update(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")
