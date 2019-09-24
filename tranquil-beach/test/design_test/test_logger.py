import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.logger import Logger

class TestKthLargest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage",
                        "shouldPrintMessage","shouldPrintMessage", "shouldPrintMessage"]
        params = [[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
        expected = [None,True,True,False,False,False,True]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()