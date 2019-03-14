import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.read4 import Read4

class TestRead4(unittest.TestCase):
    def setUp(self):
        pass

    def test_0(self):
        it = iter("abcdefghijk")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        buf = ['']*4
        self.assertEqual(read4(buf), 4)
        self.assertEqual(''.join(buf), 'abcd')
        self.assertEqual(read4(buf), 4)
        self.assertEqual(''.join(buf), 'efgh')
        self.assertEqual(read4(buf), 3)
        self.assertEqual(''.join(buf[:3]), 'ijk')

    def test_1(self):
        it = iter("abc")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        func = Read4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 1), 1)
        self.assertEqual(''.join(buf), 'a')
        buf = ['']*2
        self.assertEqual(func.read(buf, 2), 2)
        self.assertEqual(''.join(buf), 'bc')
        buf = ['']
        self.assertEqual(func.read(buf, 1), 0)
        self.assertEqual(''.join(buf), '')

if __name__ == '__main__':
    unittest.main()