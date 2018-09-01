#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Tests for the common user interface operations.

Author: Eduardo Ferreira
License: MIT (see LICENSE for details)
"""

# Module import
# --------------------------------------------------------------------------------------------------
import algos.src.bubble_sort as bubble
import unittest

# Test class
# --------------------------------------------------------------------------------------------------
class InterfaceTests(unittest.TestCase):

    def test_bubble_sort(self):
        array = [7, 3, 9, 2, 4, 1, 10, 5, 8, 6]
        bubble.bubble_sort(array)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_bubble_sort_smart(self):
        array = [7, 3, 9, 2, 4, 1, 10, 5, 8, 6]
        bubble.bubble_sort_smart(array)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_bubble_sort_smarter(self):
        array = [7, 3, 9, 2, 4, 1, 10, 5, 8, 6]
        bubble.bubble_sort_smarter(array)
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Methods :: Execution and boilerplate
# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
