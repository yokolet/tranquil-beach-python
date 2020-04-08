import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.min_swaps import MinSwaps

class TestMinSwaps(unittest.TestCase):
    def setUp(self):
        self.func = MinSwaps().minSwap
    def test_1(self):
        A, B = [1,3,5,4], [1,2,3,7]
        expected = 1
        self.assertEqual(expected, self.func(A, B))

    def test_2(self):
        A, B = [0,4,4,5,9], [0,1,6,8,10]
        expected = 1
        self.assertEqual(expected, self.func(A, B))

    def test_3(self):
        A, B = [2,1,6,9,10,13,13,16,19,26,23,24,25,27,32,31,35,36,37,39], [0,5,8,8,10,12,14,15,22,22,28,29,30,31,30,33,33,36,37,38]
        expected = 6
        self.assertEqual(expected, self.func(A, B))

    def test_4(self):
        from test_min_swaps_data import A, B
        expected = 367
        self.assertEqual(expected, self.func(A, B))

if __name__ == '__main__':
    unittest.main()
