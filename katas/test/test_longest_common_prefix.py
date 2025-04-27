import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
    
    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
    
    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")
    
    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["alone"]), "alone")
    
    def test_full_match(self):
        self.assertEqual(longest_common_prefix(["test", "test", "test"]), "test")

