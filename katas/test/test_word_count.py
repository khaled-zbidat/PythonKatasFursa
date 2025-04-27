import unittest
from katas.word_count import count_words

class TestCountWords(unittest.TestCase):
    def test_regular_sentence(self):
        sentence = "This is a simple sentence"
        self.assertEqual(count_words(sentence), 5)

    def test_empty_string(self):
        sentence = ""
        self.assertEqual(count_words(sentence), 0)

    def test_sentence_with_extra_spaces(self):
        sentence = "   Hello    world   "
        self.assertEqual(count_words(sentence), 2)

    def test_one_word(self):
        sentence = "Word"
        self.assertEqual(count_words(sentence), 1)

    def test_only_spaces(self):
        sentence = "     "
        self.assertEqual(count_words(sentence), 0)

