import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.move_zeros import MoveZeros

class TestMoveZeros(unittest.TestCase):
    def setUp(self):
        self.func = MoveZeros()

    def test_1(self):
        nums = [0,1,0,3,12]
        expected = [1,3,12,0,0]
        self.func.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_2(self):
        nums = [1]
        expected = [1]
        self.func.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_3(self):
        nums = [1, 0]
        expected = [1, 0]
        self.func.moveZeroes(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()