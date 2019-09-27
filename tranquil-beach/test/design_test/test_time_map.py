import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.time_map import TimeMap

class TestTimeMap(unittest.TestCase):
    def test_1(self):
        ops = ["TimeMap","set","get","get","set","get","get"]
        params = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
        null = None
        expected = [null,null,"bar","bar",null,"bar2","bar2"]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

    def test_2(self):
        ops = ["TimeMap","set","set","get","get","get","get","get"]
        params = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        null = None
        expected = [null,null,null,"","high","high","low","low"]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()