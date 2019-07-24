import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from backtracking.generate_parentheses import GenerateParentheses
class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.func = GenerateParentheses().generateParenthesis

    def test_1(self):
        n = 3
        expected = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        self.assertCountEqual(expected, self.func(n))

if __name__ == '__main__':
    unittest.main()