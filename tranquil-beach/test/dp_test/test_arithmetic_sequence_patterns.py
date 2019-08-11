import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.arithmetic_sequence_patterns import ArithmeticSequencePatterns

class TestArithmeticSequencePatterns(unittest.TestCase):
    def setUp(self):
        self.func = ArithmeticSequencePatterns().numberOfArithmeticSlices

    def test_0(self):
        ary = [2, 4, 6, 8, 10]
        expected = 7
        self.assertEqual(expected, self.func(ary))

if __name__ == '__main__':
    unittest.main()