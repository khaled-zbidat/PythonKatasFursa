
import unittest
from katas.list_flatten import   flat_list



class TestFlattenList(unittest.TestCase):
    
    def test_flatten_list_basic(self):
        nested_list = [1, [2, 3], [4, [5, 6]], 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list(nested_list), expected)
    
    def test_flatten_list_empty(self):
        nested_list = []
        expected = []
        self.assertEqual(flatten_list(nested_list), expected)
    
    def test_flatten_list_single_level(self):
        nested_list = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(flatten_list(nested_list), expected)
    
    def test_flatten_list_multiple_nested_levels(self):
        nested_list = [1, [2, [3, [4]]], 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list(nested_list), expected)
    
    def test_flatten_list_no_nested_lists(self):
        nested_list = [10, 20, 30]
        expected = [10, 20, 30]
        self.assertEqual(flatten_list(nested_list), expected)

    def test_flatten_list_all_empty_lists(self):
        nested_list = [[], [], []]
        expected = []
        self.assertEqual(flatten_list(nested_list), expected)

