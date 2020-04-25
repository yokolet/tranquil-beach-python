import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.rectangle_sum import RectangleSum

class TestRectangleSum(unittest.TestCase):
    def setUp(self):
        self.func = RectangleSum().maxSumSubmatrix

    def test_1(self):
        matrix, k = [[1,0,1],[0,-2,3]], 2
        expected = 2
        self.assertEqual(expected, self.func(matrix, k))

    def test_2(self):
        matrix, k = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], 10
        expected = 10
        self.assertEqual(expected, self.func(matrix, k))

if __name__ == '__main__':
    unittest.main()
