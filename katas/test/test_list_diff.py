import unittest
from katas.list_diff import find_difference

class Testlistdifference(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_difference([]), 0)

    def test_positive_and_negative(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_single_value(self):
        self.assertEqual(find_difference([7]), 0)

    def test_all_same_values(self):
        self.assertEqual(find_difference([4, 4, 4, 4]), 0)