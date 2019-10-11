import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.hit_counter import HitCounter

class TestHitCounter(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        ops = ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]
        params = [[],[1],[2],[3],[4],[300],[300],[301]]
        null = None
        expected = [null,null,null,null,3,null,4,3]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()