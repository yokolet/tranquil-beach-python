import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.count_elements import CountElements

class TestCountElements(unittest.TestCase):
    def setUp(self):
        self.func = CountElements().countElements

    def test_1(self):
        arr = [1,2,3]
        expected = 2
        self.assertEqual(self.func(arr), expected)

    def test_2(self):
        arr = [1,1,3,3,5,5,7,7]
        expected = 0
        self.assertEqual(self.func(arr), expected)

    def test_3(self):
        arr = [1,3,2,3,5,0]
        expected = 3
        self.assertEqual(self.func(arr), expected)

    def test_4(self):
        arr = [1,1,2,2]
        expected = 2
        self.assertEqual(self.func(arr), expected)

    def test_5(self):
        arr = [1,1,2]
        expected = 2
        self.assertEqual(self.func(arr), expected)

if __name__ == '__main__':
    unittest.main()