import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.interval import Interval
from sorting_searching.merge_intervals import MergeIntervals

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.func = MergeIntervals()

    def test_1(self):
        arr = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        intervals = [Interval(s, e) for [s, e] in arr]
        self.assertEqual([[i.start, i.end] for i in self.func.merge(intervals)], expected)

    def test_2(self):
        arr = [[1,4],[4,5]]
        expected = [[1,5]]
        intervals = [Interval(s, e) for [s, e] in arr]
        self.assertEqual([[i.start, i.end] for i in self.func.merge(intervals)], expected)

if __name__ == '__main__':
    unittest.main()