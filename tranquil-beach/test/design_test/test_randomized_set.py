import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.randomized_set import RandomizedSet

class TestRandomizedSet(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ['RandomizedSet','insert','remove','insert',
                'getRandom','remove','insert','getRandom']
        params = [[],[1],[2],[2],[],[1],[2],[]]
        # expected = [null,true,false,true,2,true,false,2]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)

    def test_2(self):
        ops = ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
        params = [[],[0],[1],[0],[2],[1],[]]
        # expected = [null,true,true,true,true,true,2]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)

    def test_3(self):
        ops = ["RandomizedSet","insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
        params = [[],[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]
        # expected = [null,true,true,true,false,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        print(result)

if __name__ == '__main__':
    unittest.main()