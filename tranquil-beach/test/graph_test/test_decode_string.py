import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.decode_string import DecodeString

class TestDecodeString(unittest.TestCase):
    def setUp(self):
        self.func = DecodeString().decodeString

    def test_1(self):
        s = '3[a]2[bc]'
        expected = 'aaabcbc'
        self.assertEqual(expected, self.func(s))
    
    def test_2(self):
        s = '3[a2[c]]'
        expected = 'accaccacc'
        self.assertEqual(expected, self.func(s))

    def test_3(self):
        s = '2[abc]3[cd]ef'
        expected = 'abcabccdcdcdef'
        self.assertEqual(expected, self.func(s))

    def test_4(self):
        s = '3[a]2[b4[F]c]'
        expected = 'aaabFFFFcbFFFFc'
        self.assertEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()
