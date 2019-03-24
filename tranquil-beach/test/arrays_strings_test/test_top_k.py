import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.top_k import TopK

class TestTopK(unittest.TestCase):
    def setUp(self):
        self.func = TopK()

    def test_1(self):
        nums, k = [1,1,1,2,2,3], 2
        expected = [1,2]
        self.assertEquals(self.func.topKFrequent(nums, k), expected)

    def test_2(self):
        nums, k = [1], 1
        expected = [1]
        self.assertEquals(self.func.topKFrequent(nums, k), expected)

if __name__ == '__main__':
    unittest.main()