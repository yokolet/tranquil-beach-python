import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.string_shifts import StringShifts

class TestStringShifts(unittest.TestCase):
    def setUp(self):
        self.func = StringShifts().stringShift

    def test_1(self):
        s, shift = "abc", [[0,1],[1,2]]
        expected = "cab"
        self.assertEqual(self.func(s, shift), expected)

    def test_2(self):
        s, shift = "abcdefg", [[1,1],[1,1],[0,2],[1,3]]
        expected = "efgabcd"
        self.assertEqual(self.func(s, shift), expected)

    def test_3(self):
        s, shift = "mecsk", [[1,4],[0,5],[0,4],[1,1],[1,5]]
        expected = "kmecs"
        self.assertEqual(self.func(s, shift), expected)

    def test_4(self):
        s, shift = "wpdhhcj", [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
        expected = "hcjwpdh"
        self.assertEqual(self.func(s, shift), expected)

if __name__ == '__main__':
    unittest.main()
