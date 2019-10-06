import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.letter_permutation import LetterPermutation

class TestLetterPermutation(unittest.TestCase):
    def setUp(self):
        self.func = LetterPermutation().letterCasePermutation

    def test_1(self):
        s = 'a1b2'
        expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
        self.assertCountEqual(expected, self.func(s))

    def test_2(self):
        s = '3z4'
        expected = ["3z4", "3Z4"]
        self.assertCountEqual(expected, self.func(s))

    def test_3(self):
        s = '12345'
        expected = ["12345"]
        self.assertCountEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()