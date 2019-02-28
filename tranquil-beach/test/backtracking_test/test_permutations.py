import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.permutations import Permutations

class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.func = Permutations()

    def test_1(self):
        nums = [1, 2, 3]
        expected =\
            [
                [1,2,3],
                [1,3,2],
                [2,1,3],
                [2,3,1],
                [3,1,2],
                [3,2,1]
            ]
        self.assertEqual(self.func.permute(nums), expected)

if __name__ == '__main__':
    unittest.main()