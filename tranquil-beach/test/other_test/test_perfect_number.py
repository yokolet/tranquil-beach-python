import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.perfect_number import PerfectNumber

class TestPerfectNumber(unittest.TestCase):
    def setUp(self):
        self.func = PerfectNumber()

    def test_1(self):
        num = 28
        self.assertTrue(self.func.checkPerfectNumber(num))

    def test_2(self):
        num = 1
        self.assertFalse(self.func.checkPerfectNumber(num))

if __name__ == '__main__':
    unittest.main()