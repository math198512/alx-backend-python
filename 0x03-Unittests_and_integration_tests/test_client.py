#!/usr/bin/env python3
"""Testings for the Client module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """to test utils.get_json"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org):
        """"""
        m = Mock()
        m.json.return_value = {"key": "value"}
        with patch('requests.get', return_value=m) as m:
            g = GithubOrgClient(org)
            self.assertEqual(g.org, m().json())
            m.assert_called_once()
