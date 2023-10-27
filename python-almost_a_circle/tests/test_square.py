#!/usr/bin/python3
"""Module to test square.py"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertIsNotNone(s2.id)

        s3 = Square(3, 1, 1, 12)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 1)
        self.assertEqual(s3.id, 12)

    def test_str(self):
        s1 = Square(5, 2, 1, 9)
        self.assertEqual(str(s1), "[Square] (9) 2/1 - 5")

        s2 = Square(10, 0, 0, 8)
        self.assertEqual(str(s2), "[Square] (8) 0/0 - 10")

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -10

    def test_update(self):
        s1 = Square(5, 0, 0, 1)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(10, 2)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 2")

        s1.update(10, 2, 3)
        self.assertEqual(str(s1), "[Square] (10) 3/0 - 2")

        s1.update(10, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 3/4 - 2")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        expected = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(s1_dict, expected)
