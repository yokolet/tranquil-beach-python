import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.palindrome_pairs import PalindromePairs

class TestPalindromePairs(unittest.TestCase):
    def setUp(self):
        self.func = PalindromePairs()

    def test_1(self):
        words = ["abcd","dcba","lls","s","sssll"]
        expected = [[0,1],[1,0],[3,2],[2,4]] 
        self.assertEqual(self.func.palindromePairs(words), expected)

    def test_2(self):
        words = ["bat","tab","cat"]
        expected = [[0,1],[1,0]]
        self.assertEqual(self.func.palindromePairs(words), expected)

if __name__ == '__main__':
    unittest.main()
