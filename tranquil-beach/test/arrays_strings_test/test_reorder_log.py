import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.reorder_log import ReorderLog

class TestReorderLog(unittest.TestCase):
    def setUp(self):
        self.func = ReorderLog()

    def test_1(self):
        logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        expected = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
        self.assertEqual(self.func.reorderLogFiles(logs), expected)

if __name__ == '__main__':
    unittest.main()