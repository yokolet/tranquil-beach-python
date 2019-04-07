import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.closest_palindrome import ClosestPalindrome

class TestClosestPalindrome(unittest.TestCase):
    def setUp(self):
        self.func = ClosestPalindrome()

    def test_1(self):
        n = "123"
        expected = "121"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_2(self):
        n = "9"
        expected = "8"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_3(self):
        n = "1"
        expected = "0"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_4(self):
        n = "191"
        expected = "181"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_5(self):
        n = "12"
        expected = "11"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_6(self):
        n = "10"
        expected = "9"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

    def test_7(self):
        n = "100"
        expected = "99"
        self.assertEqual(self.func.nearestPalindromic(n), expected)

if __name__ == '__main__':
    unittest.main()