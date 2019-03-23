import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.count_palindromes import CountPalindromes

class TestCountPalindromes(unittest.TestCase):
    def setUp(self):
        self.func = CountPalindromes()

    def test_1(self):
        s = "abc"
        expected = 3
        self.assertEqual(self.func.countSubstrings(s), expected)

    def test_2(self):
        s = "aaa"
        expected = 6
        self.assertEqual(self.func.countSubstrings(s), expected)

if __name__ == '__main__':
    unittest.main()