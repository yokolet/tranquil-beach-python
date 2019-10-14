import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.trie import Trie

class TestTimeMap(unittest.TestCase):
    def test_1(self):
        ops = ["Trie","insert","search","search","startsWith","insert","search"]
        params = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
        null, true, false = None, True, False
        expected = [null,null,true,false,true,null,true]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()