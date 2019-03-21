import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.most_common import MostCommon

class TestMostCommon(unittest.TestCase):
    def setUp(self):
        self.func = MostCommon()

    def test_1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        expected = "ball"
        self.assertEqual(self.func.mostCommonWord(paragraph, banned), expected)

if __name__ == '__main__':
    unittest.main()