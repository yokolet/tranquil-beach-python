import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.queens import Queens

class TestQueens(unittest.TestCase):
    def setUp(self):
        self.func = Queens().solveNQueens

    def test_1(self):
        n = 4
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        self.assertCountEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()