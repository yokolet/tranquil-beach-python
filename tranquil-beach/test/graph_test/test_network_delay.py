import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.network_delay import NetworkDelay

class TestNetworkDelay(unittest.TestCase):
    def setUp(self):
        self.func = NetworkDelay().networkDelayTime

    def test_1(self):
        times, N, K = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
        expected = 2
        self.assertEqual(expected, self.func(times, N, K))

    def test_2(self):
        times, N, K = [[1,2,1]], 2, 2
        expected = -1
        self.assertEqual(expected, self.func(times, N, K))

    def test_3(self):
        times, N, K = [[1,2,1],[2,3,2],[1,3,4]], 3, 1
        expected = 3
        self.assertEqual(expected, self.func(times, N, K))

    def test_4(self):
        times, N, K = [[1,2,1],[2,1,3]], 2, 2
        expected = 3
        self.assertEqual(expected, self.func(times, N, K))

    def test_5(self):
        times, N, K = [[1,2,1],[2,3,2],[1,3,1]], 3, 2
        expected = -1
        self.assertEqual(expected, self.func(times, N, K))

if __name__ == '__main__':
    unittest.main()
