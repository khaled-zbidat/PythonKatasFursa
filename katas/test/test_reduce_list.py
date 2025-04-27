import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):
    def test_normal_case(self):
        numbers = [5, 10, 15]
        reduce_array(numbers)
        self.assertEqual(numbers, [5, 5, 5])

    def test_single_element(self):
        numbers = [7]
        reduce_array(numbers)
        self.assertEqual(numbers, [7])

    def test_empty_list(self):
        numbers = []
        reduce_array(numbers)
        self.assertEqual(numbers, [])

    def test_negative_numbers(self):
        numbers = [-2, 3, -1, 4]
        reduce_array(numbers)
        self.assertEqual(numbers, [-2, 5, -4, 5])

    def test_large_numbers(self):
        numbers = [1000, 2000, 5000, 10000]
        reduce_array(numbers)
        self.assertEqual(numbers, [1000, 1000, 3000, 5000])

