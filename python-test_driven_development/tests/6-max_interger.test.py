#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_integer(self):
        """Test for max integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([float('inf'), float('inf'), float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('-inf')]), 3)
        self.assertEqual(max_integer([float('-inf'), float('-inf'), float('-inf')]), float('-inf'))
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, "hello", 3, 4])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], 4])
        self.assertRaises(TypeError, max_integer, [1, (2, 3), 4])
        self.assertRaises(TypeError, max_integer, [1, {2, 3}, 4])
        self.assertRaises(TypeError, max_integer, [1, {"a": 2}, 4])
        self.assertRaises(TypeError, max_integer, [1, None, 4])
        self.assertRaises(TypeError, max_integer, None)
