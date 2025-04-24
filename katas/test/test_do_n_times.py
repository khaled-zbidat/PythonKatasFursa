import unittest
from katas.do_n_times import do_n_times  

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

class TestDoNTimes(unittest.TestCase):

    def test_function_called_n_times(self):
        counter = Counter()
        do_n_times(counter.increment, 5)
        self.assertEqual(counter.count, 5)

    def test_zero_times(self):
        counter = Counter()
        do_n_times(counter.increment, 0)
        self.assertEqual(counter.count, 0)

    def test_one_time(self):
        counter = Counter()
        do_n_times(counter.increment, 1)
        self.assertEqual(counter.count, 1)

