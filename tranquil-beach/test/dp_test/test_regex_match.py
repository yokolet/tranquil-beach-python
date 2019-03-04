import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.regex_match import RegexMatch

class TestRegexMatch(unittest.TestCase):
    def setUp(self):
        self.func = RegexMatch()

    def test_1(self):
        s, p = "aa", "a"
        self.assertFalse(self.func.isMatch(s, p))

    def test_2(self):
        s, p = "aa", "a*"
        self.assertTrue(self.func.isMatch(s, p))

    def test_3(self):
        s, p = "ab", ".*"
        self.assertTrue(self.func.isMatch(s, p))

    def test_4(self):
        s, p = "aab", "c*a*b"
        self.assertTrue(self.func.isMatch(s, p))

    def test_5(self):
        s, p = "mississippi", "mis*is*p*."
        self.assertFalse(self.func.isMatch(s, p))

if __name__ == '__main__':
    unittest.main()