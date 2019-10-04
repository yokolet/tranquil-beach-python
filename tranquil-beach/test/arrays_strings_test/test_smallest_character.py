import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.smallest_character import SmallestCharacter

class TestSmallestCharacter(unittest.TestCase):
    def setUp(self):
        self.func = SmallestCharacter().numSmallerByFrequency

    def test_1(self):
        queries, words = ['cbd'], ['zaaaz']
        expected = [1]
        self.assertEqual(expected, self.func(queries, words))

    def test_2(self):
        queries, words = ['bbb','cc'], ['a','aa','aaa','aaaa']
        expected = [1,2]
        self.assertEqual(expected, self.func(queries, words))

if __name__ == '__main__':
    unittest.main()