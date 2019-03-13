import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.word_dictionary import WordDictionary

class TestSubsets(unittest.TestCase):
    def test_1(self):
        ops = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        params = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        expected = [None,None,None,None,False,True,True,True]
        func = eval(ops[0])(*params[0])
        result = [None]
        for op, param in zip(ops[1:], params[1:]):
            result.append(getattr(func, op)(*param))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()