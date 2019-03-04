import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.addition_by_string import AdditionByString

class TestAdditionByString(unittest.TestCase):
    def setUp(self):
        self.func = AdditionByString()

    def test_1(self):
        num1 = "999"
        num2 = "1"
        expected = "1000"
        self.assertEqual(self.func.addStrings(num1, num2), expected)

    def test_2(self):
        num1 = "1"
        num2 = "12345"
        expected = "12346"
        self.assertEqual(self.func.addStrings(num1, num2), expected)

if __name__ == '__main__':
    unittest.main()