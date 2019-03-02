import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.valid_parentheses import ValidParentheses

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.func = ValidParentheses()

    def test_1(self):
        s = "()"
        self.assertTrue(self.func.isValid(s))

    def test_2(self):
        s = "()[]{}"
        self.assertTrue(self.func.isValid(s))

    def test_3(self):
        s = "(]"
        self.assertFalse(self.func.isValid(s))

    def test_4(self):
        s = "([)]"
        self.assertFalse(self.func.isValid(s))

    def test_5(self):
        s = "{[]}"
        self.assertTrue(self.func.isValid(s))

if __name__ == '__main__':
    unittest.main()