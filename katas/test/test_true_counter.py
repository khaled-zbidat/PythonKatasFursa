import unittest

from katas.true_counter import count_true_values

class TestCountTrueValues(unittest.TestCase):
    def test_all_true(self):
        array = [True, True, True]
        self.assertEqual(count_true_values(array), 3)

    def test_all_false(self):
        array = [False, False, False]
        self.assertEqual(count_true_values(array), 0)

    def test_mixed_values(self):
        array = [True, False, True, False, True]
        self.assertEqual(count_true_values(array), 3)

    def test_empty_list(self):
        array = []
        self.assertEqual(count_true_values(array), 0)

    def test_no_boolean_values(self):
        array = [1, 0, None, 'True', False]
        self.assertEqual(count_true_values(array), 0)  

