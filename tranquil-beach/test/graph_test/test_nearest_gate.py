import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.nearest_gate import NearestGate

class TestNearestGate(unittest.TestCase):
    def setUp(self):
        self.func = NearestGate().wallsAndGates

    def test_1(self):
        INF = 2147483647
        rooms = [
            [INF,  -1,  0,  INF],
            [INF, INF, INF,  -1],
            [INF,  -1, INF,  -1],
            [  0,  -1, INF, INF]
        ]
        expected = [
            [  3,  -1,  0,   1],
            [  2,   2,  1,  -1],
            [  1,  -1,  2,  -1],
            [  0,  -1,  3,   4]
        ]
        self.func(rooms)
        self.assertEqual(expected, rooms)

if __name__ == '__main__':
    unittest.main()