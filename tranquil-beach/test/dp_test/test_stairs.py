import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.stairs import Stairs

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.func = Stairs()

    def test_1(self):
        n = 2
        expected = 2
        self.assertEqual(self.func.climbStairs(n), expected)

    def test_2(self):
        n = 3
        expected = 3
        self.assertEqual(self.func.climbStairs(n), expected)

    def test_3(self):
        n = 2
        expected = 2
        self.assertEqual(self.func.climbStairsRecur(n), expected)

    def test_4(self):
        n = 3
        expected = 3
        self.assertEqual(self.func.climbStairsRecur(n), expected)

if __name__ == '__main__':
    unittest.main()