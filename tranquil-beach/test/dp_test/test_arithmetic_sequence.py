import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.arithmetic_sequence import ArithmeticSequence

class TestArithmeticSequence(unittest.TestCase):
    def setUp(self):
        self.func = ArithmeticSequence().longestArithSeqLength

    def test_0(self):
        ary = [3,6,9,12]
        expected = 4
        self.assertEqual(expected, self.func(ary))

    def test_1(self):
        ary = [9,4,7,2,10]
        expected = 3
        self.assertEqual(expected, self.func(ary))

    def test_2(self):
        ary = [20,1,15,3,10,5,8]
        expected = 4
        self.assertEqual(expected, self.func(ary))

if __name__ == '__main__':
    unittest.main()