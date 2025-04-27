import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_mixed_characters(self):
        self.assertEqual(sum_of_digits("abc123"), 6)

    def test_only_digits(self):
        self.assertEqual(sum_of_digits("4567"), 22)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("hello"), 0)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_digits_with_special_characters(self):
        self.assertEqual(sum_of_digits("1a2!3@4#"), 10)

