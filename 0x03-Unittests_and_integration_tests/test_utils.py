#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """the first unit test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method to test test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
