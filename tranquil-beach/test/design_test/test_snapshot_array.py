import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.snapshot_array import SnapshotArray

class TestSnapshotArray(unittest.TestCase):
    def test_1(self):
        ops = ["SnapshotArray","set","snap","set","get"]
        params = [[3],[0,5],[],[0,6],[0,0]]
        null = None
        expected = [null,null,0,null,5]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
