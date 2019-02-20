import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.combination_sum import CombinationSum

class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.func = CombinationSum()

    def test_1(self):
        candidates = [2,3,6,7]
        target = 7
        expected = [[7], [2,2,3]]
        self.assertCountEqual(self.func.combinationSum(candidates, target), expected)

    def test_2(self):
        candidates = [2,3,5]
        target = 8
        expected = [[2,2,2,2],[2,3,3],[3,5]]
        self.assertCountEqual(self.func.combinationSum(candidates, target), expected)

if __name__ == '__main__':
    unittest.main()