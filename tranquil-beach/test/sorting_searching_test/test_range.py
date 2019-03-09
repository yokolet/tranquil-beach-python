import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.range import Range

class TestRange(unittest.TestCase):
    def setUp(self):
        self.func = Range()

    def test_1(self):
        nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
        expected = [20,24]
        self.assertEqual(self.func.smallestRange(nums), expected)

if __name__ == '__main__':
    unittest.main()