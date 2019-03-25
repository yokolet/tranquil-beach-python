import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.peak_element import PeakElement

class TestPeakElement(unittest.TestCase):
    def setUp(self):
        self.func = PeakElement()

    def test_1(self):
        nums = [1,2,3,1]
        expected = 2
        self.assertEqual(self.func.findPeakElement(nums), expected)

    def test_2(self):
        nums = [1,2,1,3,5,6,4]
        expected = [1, 5]
        self.assertIn(self.func.findPeakElement(nums), expected)

if __name__ == '__main__':
    unittest.main()