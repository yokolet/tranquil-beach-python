import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from graph.evaluate_division import EvaluateDivision

class TestEvaluateDivision(unittest.TestCase):
    def setUp(self):
        self.func = EvaluateDivision().calcEquation

    def test_1(self):
        equations, values, queries = [["a","b"],["b","c"]], [2.0, 3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        expected = [6.0,0.5,-1.0,1.0,-1.0]
        self.assertEqual(self.func(equations, values, queries), expected)

if __name__ == '__main__':
    unittest.main()
