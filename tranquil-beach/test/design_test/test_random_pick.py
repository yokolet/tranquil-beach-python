import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.random_pick import RandomPick

class TestRandomPick(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["RandomPick","pickIndex"]
        params = [[[1]],[]]
        expected = [None,0]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)
        #self.assertCountEqual(result, expected)
    
    def test_2(self):
        ops = ["RandomPick","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
        params = [[[1,3]],[],[],[],[],[]]
        expected = [None,0,1,1,1,0]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)
        #self.assertCountEqual(result, expected)

if __name__ == '__main__':
    unittest.main()