import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.max_in_window import MaxInWindow

class TestMaxInWindow(unittest.TestCase):
    def setUp(self):
        self.func = MaxInWindow().maxSlidingWindow

    def test_1(self):
        nums, k = [1,3,-1,-3,5,3,6,7], 3
        expected = [3,3,5,5,6,7]
        self.assertEqual(expected, self.func(nums, k))

if __name__ == '__main__':
    unittest.main()