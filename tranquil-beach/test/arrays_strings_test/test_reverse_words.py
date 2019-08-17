import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.reverse_words import ReverseWords

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.func = ReverseWords().reverseWords

    def test_1(self):
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(expected, self.func(s))

    def test_2(self):
        s = "  hello world!  "
        expected = "world! hello"
        self.assertEqual(expected, self.func(s))

    def test_3(self):
        s = "a good   example"
        expected = "example good a"
        self.assertEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()