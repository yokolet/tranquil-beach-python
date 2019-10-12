import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.merge_intervals import MergeIntervals

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.func = MergeIntervals().merge

    def test_1(self):
        arr = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(expected, self.func(arr))

    def test_2(self):
        arr = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(expected, self.func(arr))

if __name__ == '__main__':
    unittest.main()