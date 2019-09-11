import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.package_shipping import PackageShipping

class TestPackageShipping(unittest.TestCase):
    def setUp(self):
        self.func = PackageShipping().shipWithinDays

    def test_1(self):
        weights, d = [1,2,3,4,5,6,7,8,9,10], 5
        expected = 15
        self.assertEqual(expected, self.func(weights, d))

    def test_2(self):
        weights, d = [3,2,2,4,1,4], 3
        expected = 6
        self.assertEqual(expected, self.func(weights, d))

    def test_3(self):
        weights, d = [1,2,3,1,1], 4
        expected = 3
        self.assertEqual(expected, self.func(weights, d))

if __name__ == '__main__':
    unittest.main()