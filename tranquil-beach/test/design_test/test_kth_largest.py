import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.kth_largest import KthLargest
from design.kth_largest_bst import KthLargestBst

class TestKthLargest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["KthLargest","add","add","add","add","add"]
        params = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
        expected = [None,4,5,5,8,8]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

    def test_2(self):
        ops = ["KthLargestBst","add","add","add","add","add"]
        params = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
        expected = [None,4,5,5,8,8]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()