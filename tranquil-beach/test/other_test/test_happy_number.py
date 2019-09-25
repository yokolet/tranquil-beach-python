import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.happy_number import HappyNumber

class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.func = HappyNumber().isHappy

    def test_1(self):
        n = 19
        self.assertTrue(self.func(n))

if __name__ == '__main__':
    unittest.main()