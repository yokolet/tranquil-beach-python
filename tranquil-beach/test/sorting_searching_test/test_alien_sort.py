import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.alien_sort import AlienSort

class TestAlienSort(unittest.TestCase):
    def setUp(self):
        self.func = AlienSort().isAlienSorted

    def test_1(self):
        words, order = ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.func(words, order))

    def test_2(self):
        words, order = ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(self.func(words, order))

    def test_3(self):
        words, order = ["apple","app"], "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.func(words, order))

    def test_4(self):
        words, order = ["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"
        self.assertTrue(self.func(words, order))

if __name__ == '__main__':
    unittest.main()