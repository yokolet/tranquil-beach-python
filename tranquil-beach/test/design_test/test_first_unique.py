import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.first_unique import FirstUnique

class TestFirstUnique(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
        params = [[[2,3,5]],[],[5],[],[2],[],[3],[]]
        null = None
        expected = [null,2,null,2,null,3,null,-1]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)

    def test_2(self):
        ops = ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
        params = [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
        null = None
        expected = [null,-1,null,null,null,null,null,17]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)

    def test_3(self):
        ops = ["FirstUnique","showFirstUnique","add","showFirstUnique"]
        params = [[[809]],[],[809],[]]
        null = None
        expected = [null,809,null,-1]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)

    def test_4(self):
        null = None
        from test_first_unique_data import ops, params, expected
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
