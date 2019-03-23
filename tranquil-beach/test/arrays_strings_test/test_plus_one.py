import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.plus_one import PlusOne

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.func = PlusOne()

    def test_1(self):
        digits = [1,2,3]
        expected = [1,2,4]
        self.assertEqual(self.func.plusOne(digits), expected)

    def test_2(self):
        digits = [4,3,2,1]
        expected = [4,3,2,2]
        self.assertEqual(self.func.plusOne(digits), expected)

    def test_3(self):
        digits = [4,3,9,9]
        expected = [4,4,0,0]
        self.assertEqual(self.func.plusOne(digits), expected)

    def test_4(self):
        digits = [9]
        expected = [1,0]
        self.assertEqual(self.func.plusOne(digits), expected)

if __name__ == '__main__':
    unittest.main()