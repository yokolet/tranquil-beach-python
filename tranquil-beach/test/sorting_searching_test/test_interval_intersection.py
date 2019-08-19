import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.interval_intersection import IntervalIntersection

class TestIntervalIntersection(unittest.TestCase):
    def setUp(self):
        self.func = IntervalIntersection().intervalIntersection

    def test_1(self):
        A, B = [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
        expected = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertEqual(expected, self.func(A, B))

    def test_2(self):
        A, B = [[1,3],[5,9]], []
        expected = []
        self.assertEqual(expected, self.func(A, B))

if __name__ == '__main__':
    unittest.main()