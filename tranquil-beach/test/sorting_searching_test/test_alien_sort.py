import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.alien_sort import AlienSort

class TestAlienSort(unittest.TestCase):
    def setUp(self):
        self.func = AlienSort()

    def test_1(self):
        words, order = ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.func.isAlienSorted(words, order))

    def test_2(self):
        words, order = ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(self.func.isAlienSorted(words, order))

    def test_3(self):
        words, order = ["apple","app"], "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.func.isAlienSorted(words, order))

if __name__ == '__main__':
    unittest.main()