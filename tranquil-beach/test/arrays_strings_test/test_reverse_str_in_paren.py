import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.reverse_str_in_paren import ReverseStrInParen

class TestReverseStrInParen(unittest.TestCase):
    def setUp(self):
        self.func = ReverseStrInParen().reverseParentheses

    def test_1(self):
        s = '(abcd)'
        expected = 'dcba'
        self.assertEqual(expected, self.func(s))

    def test_2(self):
        s = '(u(love)i)'
        expected = 'iloveu'
        self.assertEqual(expected, self.func(s))

    def test_3(self):
        s = '(ed(et(oc))el)'
        expected = 'leetcode'
        self.assertEqual(expected, self.func(s))

    def test_4(self):
        s = 'a(bcdefghijkl(mno)p)q'
        expected = 'apmnolkjihgfedcbq'
        self.assertEqual(expected, self.func(s))

    def test_5(self):
        s = '((eqk((h))))'
        expected = 'eqkh'
        self.assertEqual(expected, self.func(s))

    def test_6(self):
        s = 'ta()usw((((a))))'
        expected = 'tauswa'
        self.assertEqual(expected, self.func(s))

    def test_7(self):
        s = 's()uteawj((eg))'
        expected = 'suteawjeg'
        self.assertEqual(expected, self.func(s))

    def test_8(self):
        s = 'sxmdll(q)eki(x)'
        expected = 'sxmdllqekix'
        self.assertEqual(expected, self.func(s))

    def test_9(self):
        s = 'f(ul)ao(t(y)qbn)()sj'
        expected = 'fluaonbqytsj'
        self.assertEqual(expected, self.func(s))

if __name__ == '__main__':
    unittest.main()