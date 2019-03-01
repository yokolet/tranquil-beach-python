import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.permutations_with_dup import PermutationsWithDup

class TestPermutationsWithDup(unittest.TestCase):
    def setUp(self):
        self.func = PermutationsWithDup()

    def test_1(self):
        nums = [1, 1, 2]
        expected =\
            [
                [1,1,2],
                [1,2,1],
                [2,1,1]
            ]
        self.assertEqual(self.func.permuteUnique(nums), expected)

    def test_2(self):
        nums = [2,2,1,1]
        expected = [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
        self.assertEqual(self.func.permuteUnique(nums), expected)

if __name__ == '__main__':
    unittest.main()