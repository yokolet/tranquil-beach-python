import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.k_closest import KClosest

class TestKClosest(unittest.TestCase):
    def setUp(self):
        self.func = KClosest()

    def test_1(self):
        points, K = [[1,3],[-2,2]], 1
        expected = [[-2,2]]
        self.assertEqual(self.func.kClosest(points, K), expected)


    def test_2(self):
        points, K = [[3,3],[5,-1],[-2,4]], 2
        expected = [[3,3],[-2,4]]
        self.assertCountEqual(self.func.kClosest(points, K), expected)

if __name__ == '__main__':
    unittest.main()