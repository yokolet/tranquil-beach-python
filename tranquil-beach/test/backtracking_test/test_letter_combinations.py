import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.letter_combinations import LetterCombinations

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.func = LetterCombinations()
    
    def test_1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = self.func.letterCombinations(digits)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
