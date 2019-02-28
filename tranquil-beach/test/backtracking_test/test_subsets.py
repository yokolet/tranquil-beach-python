import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.subsets import Subsets

class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.func = Subsets()

    def test_1(self):
        nums = [1,2,3]
        expected = [
            [3],
            [1],
            [2],
            [1,2,3],
            [1,3],
            [2,3],
            [1,2],
            []
            ]
        self.assertEqual(sorted(self.func.subsets(nums)), sorted(expected))

if __name__ == '__main__':
    unittest.main()