import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.invalid_parentheses import InvalidParentheses

class TestInvalidParentheses(unittest.TestCase):
    def setUp(self):
        self.func = InvalidParentheses()

    def test_1(self):
        s = "()())()"
        expected = ["()()()", "(())()"]
        self.assertCountEqual(self.func.removeInvalidParentheses(s), expected)

    def test_2(self):
        s = "(a)())()"
        expected = ["(a)()()", "(a())()"]
        self.assertCountEqual(self.func.removeInvalidParentheses(s), expected)

    def test_3(self):
        s = ")("
        expected = [""]
        self.assertCountEqual(self.func.removeInvalidParentheses(s), expected)

if __name__ == '__main__':
    unittest.main()