import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.arithmetic_slice import ArithmeticSlice

class TestArithmeticSlice(unittest.TestCase):
    def setUp(self):
        self.func = ArithmeticSlice().numberOfArithmeticSlices

    def test_0(self):
        ary = [1, 2, 3, 4]
        expected = 3
        self.assertEqual(expected, self.func(ary))

if __name__ == '__main__':
    unittest.main()