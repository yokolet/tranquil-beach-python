import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.func = Product()

    def test_1(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        self.assertEqual(self.func.productExceptSelf(nums), expected)

if __name__ == '__main__':
    unittest.main()