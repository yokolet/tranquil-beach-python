import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.divide_chocolate import DivideChocolate

class TestDivideChocolate(unittest.TestCase):
    def setUp(self):
        self.func = DivideChocolate().maximizeSweetness

    def test_1(self):
        s, k = [1,2,3,4,5,6,7,8,9], 5
        expected = 6
        self.assertEqual(expected, self.func(s, k))

    def test_2(self):
        s, k = [5,6,7,8,9,1,2,3,4], 8
        expected = 1
        self.assertEqual(expected, self.func(s, k))

    def test_3(self):
        s, k = [1,2,2,1,2,2,1,2,2], 2
        expected = 5
        self.assertEqual(expected, self.func(s, k))

    def test_4(self):
        s, k = [19679,20653,68010,3714,54485,548,41366,11201,47138,70768,1050,87246,17114,56157,13235,65363,30444,56929,21969,22308], 0
        expected = sum(s)
        self.assertEqual(expected, self.func(s, k))

    def test_5(self):
        s, k = [87002,22650,61737,4432,87341,67643,13454,83823,87836,2978,99313,82797,77350,55994,31403,
                73836,54451,54807,60146,72381,7271,37633,32603,33752,78004,76288,94608,3516,98287,16577,
                36186,40401,70733,35764,76303,74279,18351,74113,26480,64253,49402,47512,37185,42488,43068,
                3542,55773,91365,86770,52915], 3
        expected = 641293
        self.assertEqual(expected, self.func(s, k))

if __name__ == '__main__':
    unittest.main()
