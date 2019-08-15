import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.histogram import Histogram

class TestHistogram(unittest.TestCase):
    def setUp(self):
        self.func = Histogram().largestRectangleArea

    def test_1(self):
        heights = [2,1,5,6,2,3]
        expected = 10
        self.assertEqual(expected, self.func(heights))

    def test_2(self):
        heights = [6,2,5,4,5,1,6]
        expected = 12
        self.assertEqual(expected, self.func(heights))

    def test_3(self):
        heights = [6,2,5,4,5,2,6]
        expected = 14
        self.assertEqual(expected, self.func(heights))

if __name__ == '__main__':
    unittest.main()