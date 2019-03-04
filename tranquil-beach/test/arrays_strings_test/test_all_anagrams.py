import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.all_anagrams import AllAnagrams

class TestAllAnagrams(unittest.TestCase):
    def setUp(self):
        self.func = AllAnagrams()

    def test_1(self):
        s, p = "cbaebabacd", "abc"
        expected = [0, 6]
        self.assertEqual(self.func.findAnagrams(s, p), expected)

    def test_2(self):
        s, p = "abab", "ab"
        expected = [0, 1, 2]
        self.assertEqual(self.func.findAnagrams(s, p), expected)

    def test_3(self):
        s, p = "abaacbabc", "abc"
        expected = [3,4,6]
        self.assertEqual(self.func.findAnagrams(s, p), expected)

if __name__ == '__main__':
    unittest.main()