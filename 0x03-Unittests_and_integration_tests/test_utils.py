#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest, parameterized

class TestAccessNestedMap(unittest.TestCase):
    """the first unit test for utils.access_nested_map"""
    def test_access_nested_map(self):
        self.assertEqual(nested_map={"a": 1}, path=("a",))
    