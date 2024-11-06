#!/usr/bin/env python3
"""Testings for the Client module"""
import unittest
from parameterized import parameterized
from unittest.mock import MagicMock, patch, Mock
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """to test utils.get_json"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=input))
