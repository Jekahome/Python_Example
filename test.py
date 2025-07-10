#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from base import add

class UnitTest(unittest.TestCase):

    def test_add(self):

        expected = 5
        actual = add(2, 3)
        self.assertEqual(expected, actual)
