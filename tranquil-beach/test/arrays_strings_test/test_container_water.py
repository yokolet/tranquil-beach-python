import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.container_water import ContainerWater

class TestContainerWater(unittest.TestCase):
    def setUp(self):
        self.func = ContainerWater().maxArea

    def test_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected = 49
        self.assertEquals(expected, self.func(height))

if __name__ == '__main__':
    unittest.main()