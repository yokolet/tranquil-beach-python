import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.next_closest_time import NextClosestTime

class TestNextClosestTime(unittest.TestCase):
    def setUp(self):
        self.func = NextClosestTime().nextClosestTime

    def test_1(self):
        time  = '19:34'
        expected = '19:39'
        self.assertEqual(expected, self.func(time))

    def test_2(self):
        time  = '23:59'
        expected = '22:22'
        self.assertEqual(expected, self.func(time))

if __name__ == '__main__':
    unittest.main()