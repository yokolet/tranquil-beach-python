import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.monotonic import Monotonic

class TestMonotonic(unittest.TestCase):
    def setUp(self):
        self.func = Monotonic()

    def test_1(self):
        nums = [1,2,2,3]
        self.assertTrue(self.func.isMonotonic(nums))
    
    def test_2(self):
        nums = [6,5,4,4]
        self.assertTrue(self.func.isMonotonic(nums))
    
    def test_3(self):
        nums = [1,3,2]
        self.assertFalse(self.func.isMonotonic(nums))
    
    def test_4(self):
        nums = [1,2,4,5]
        self.assertTrue(self.func.isMonotonic(nums))
    
    def test_5(self):
        nums = [1,1,1]
        self.assertTrue(self.func.isMonotonic(nums))

if __name__ == '__main__':
    unittest.main()