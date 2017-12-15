# -*- coding: utf-8 -*-

import unittest

import addresslib


class ParserTest(unittest.TestCase):
    def test_single_address(self):
        address = addresslib.parse('joe@example.com')
        self.assertEqual('', address.display_name)
        self.assertEqual('joe', address.username)
        self.assertEqual('example.com', address.domain)

        address = addresslib.parse('<joe@example.com>')
        self.assertEqual('', address.display_name)
        self.assertEqual('joe', address.username)
        self.assertEqual('example.com', address.domain)

        address = addresslib.parse('Jane Doe <Jane@example.com>')
        self.assertEqual('Jane Doe', address.display_name)
        self.assertEqual('Jane', address.username)
        self.assertEqual('example.com', address.domain)

    def test_multiple_addresses(self):
        addresses = addresslib.parse_list(
            'joe@example.com, <joe@example.com>, Jane Doe <jane@example.com>'
        )
        self.assertEqual(3, len(addresses))

    def test_string_representation(self):
        address = addresslib.parse('Jane Doe <jane@example.com>')
        self.assertEqual('Jane Doe <jane@example.com>', str(address))

        address = addresslib.Address(
            display_name='Jane Doe', addr_spec='jane@example.com'
        )
        self.assertEqual('Jane Doe <jane@example.com>', str(address))
