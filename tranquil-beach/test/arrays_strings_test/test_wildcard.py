import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.wildcard import Wildcard

class TestWildcard(unittest.TestCase):
    def setUp(self):
        self.func = Wildcard()

    def test_1(self):
        s, p = "aa", "a"
        self.assertFalse(self.func.isMatch(s, p))

    def test_2(self):
        s, p = "aa", "*"
        self.assertTrue(self.func.isMatch(s, p))

    def test_3(self):
        s, p = "cb", "?a"
        self.assertFalse(self.func.isMatch(s, p))

    def test_4(self):
        s, p = "adceb", "*a*b"
        self.assertTrue(self.func.isMatch(s, p))

    def test_5(self):
        s, p = "acdcb", "a*c?b"
        self.assertFalse(self.func.isMatch(s, p))

if __name__ == '__main__':
    unittest.main()