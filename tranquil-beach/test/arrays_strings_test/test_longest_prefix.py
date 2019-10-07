import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.longest_prefix import LongestPrefix

class TestLongestPrefix(unittest.TestCase):
    def setUp(self):
        self.func = LongestPrefix().longestCommonPrefix

    def test_1(self):
        words = ["flower","flow","flight"]
        expected = 'fl'
        self.assertEqual(expected, self.func(words))

    def test_2(self):
        words = ["dog","racecar","car"]
        expected = ''
        self.assertEqual(expected, self.func(words))

    def test_3(self):
        words = ["a"]
        expected = 'a'
        self.assertEqual(expected, self.func(words))

if __name__ == '__main__':
    unittest.main()