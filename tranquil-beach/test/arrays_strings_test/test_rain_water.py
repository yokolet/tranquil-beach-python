import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.rain_water import RainWater

class TestRainWater(unittest.TestCase):
    def setUp(self):
        self.func = RainWater()

    def test_1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        self.assertEqual(self.func.trap(height), expected)

if __name__ == '__main__':
    unittest.main()