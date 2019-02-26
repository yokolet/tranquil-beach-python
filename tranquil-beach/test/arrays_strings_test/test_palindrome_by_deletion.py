import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.palindrome_by_deletion import PalindromeByDeletion

class TestPalindromeByDeletion(unittest.TestCase):
    def setUp(self):
        self.func = PalindromeByDeletion()

    def test_1(self):
        s = "aba"
        self.assertTrue(self.func.validPalindrome(s))

    def test_2(self):
        s = "abca"
        self.assertTrue(self.func.validPalindrome(s))

if __name__ == '__main__':
    unittest.main()