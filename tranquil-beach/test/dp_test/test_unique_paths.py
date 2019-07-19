import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.unique_paths import UniquePaths

class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.func = UniquePaths().uniquePaths

    def test_1(self):
        m, n = 3, 2
        expected = 3
        self.assertEquals(expected, self.func(m, n))

    def test_2(self):
        m, n = 7, 3
        expected = 28
        self.assertEquals(expected, self.func(m, n))

if __name__ == '__main__':
    unittest.main()