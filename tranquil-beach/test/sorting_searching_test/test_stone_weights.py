import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.stone_weights import StoneWeights

class TestSplitArray(unittest.TestCase):
    def setUp(self):
        self.func = StoneWeights().lastStoneWeight

    def test_1(self):
        stones = [2,7,4,1,8,1]
        expected = 1
        self.assertEqual(expected, self.func(stones))

    def test_2(self):
        stones = [2,2]
        expected = 0
        self.assertEqual(expected, self.func(stones))

if __name__ == '__main__':
    unittest.main()
