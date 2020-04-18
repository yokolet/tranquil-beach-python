import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from dp.longest_string_chain import LongestStringChain

class TestLongestStringChain(unittest.TestCase):
    def setUp(self):
        self.func = LongestStringChain().longestStrChain

    def test_1(self):
        words = ["a","b","ba","bca","bda","bdca"]
        expected = 4
        self.assertEqual(self.func(words), expected)

    def test_2(self):
        words = ["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju",
                "cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc",
                "nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl",
                "ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr",
                "sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx",
                "gxi","gqxi","heheex"]
        expected = 9
        self.assertEqual(self.func(words), expected)

if __name__ == '__main__':
    unittest.main()
