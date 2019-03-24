import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.min_index_sum import MinIndexSum

class TestMinIndexSum(unittest.TestCase):
    def setUp(self):
        self.func = MinIndexSum()

    def test_1(self):
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected = ["Shogun"]
        self.assertCountEqual(self.func.findRestaurant(list1, list2), expected)

    def test_2(self):
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["KFC", "Shogun", "Burger King"]
        expected = ["Shogun"]
        self.assertCountEqual(self.func.findRestaurant(list1, list2), expected)

if __name__ == '__main__':
    unittest.main()