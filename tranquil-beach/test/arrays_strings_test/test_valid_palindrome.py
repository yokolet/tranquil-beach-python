import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.valid_palindrome import ValidPalindrome

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.func = ValidPalindrome().isPalindrome

    def test_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.func(s))

    def test_2(self):
        s = "race a car"
        self.assertFalse(self.func(s))

if __name__ == '__main__':
    unittest.main()
