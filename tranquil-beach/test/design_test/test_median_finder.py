import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.median_finder import MedianFinder

class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        params = [[],[1],[2],[],[3],[]]
        expected = [None, None, None, 1.5, None, 2.0]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)
        self.assertEquals(expected, result)

if __name__ == '__main__':
    unittest.main()