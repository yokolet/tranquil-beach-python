import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.strobogrammatic import Strobogrammatic

class TestStrobogrammatic(unittest.TestCase):
    def setUp(self):
        self.func = Strobogrammatic()

    def test_1(self):
        num =  "69"
        self.assertTrue(self.func.isStrobogrammatic(num))

    def test_2(self):
        num = "88"
        self.assertTrue(self.func.isStrobogrammatic(num))

    def test_3(self):
        num = "962"
        self.assertFalse(self.func.isStrobogrammatic(num))

if __name__ == '__main__':
    unittest.main()