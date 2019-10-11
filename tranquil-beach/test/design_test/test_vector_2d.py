import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.vector_2d import Vector2D

class TestVector2D(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]
        params = [[[[1,2],[3],[4]]],[],[],[],[],[],[],[]]
        null, true, false = None, True, False
        expected = [null,1,2,3,true,true,4,false]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()