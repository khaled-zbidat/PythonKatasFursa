import unittest
import time 
from katas.time_me import measure_execution_time

class TestTimeMe(unittest.TestCase):
    def test_quick_function(self):
        def quick_function():
            return sum(range(10))
        
        exec_time = measure_execution_time(quick_function)
        self.assertGreaterEqual(exec_time, 0)  

    def test_sleep_function(self):
        def sleep_function():
            time.sleep(0.1)  
        
        exec_time = measure_execution_time(sleep_function)
        self.assertGreaterEqual(exec_time, 100)  
        self.assertLess(exec_time, 200)  

    def test_instant_function(self):
        def instant_function():
            pass
        
        exec_time = measure_execution_time(instant_function)
        self.assertLess(exec_time, 10)  

