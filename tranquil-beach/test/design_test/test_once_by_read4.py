import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from design.once_by_read4 import OnceByRead4

class TestOnceByRead4(unittest.TestCase):
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
        func = OnceByRead4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 4), 3)
        self.assertEqual(''.join(buf), 'abc')

    def test_2(self):
        it = iter("abcde")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        func = OnceByRead4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 5), 5)
        self.assertEqual(''.join(buf), 'abcde')

    def test_3(self):
        it = iter("abcdABCD1234")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        func = OnceByRead4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 12), 12)
        self.assertEqual(''.join(buf), 'abcdABCD1234')

    def test_4(self):
        it = iter("leetcode")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        func = OnceByRead4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 5), 5)
        self.assertEqual(''.join(buf), 'leetc')

    def test_5(self):
        it = iter("abcd")
        def read4(buf):
            index = 0
            try:
                while index < 4:
                    buf[index] = next(it)
                    index += 1
            except StopIteration:
                pass
            return index
        func = OnceByRead4(read4)
        buf = ['']
        self.assertEqual(func.read(buf, 5), 4)
        self.assertEqual(''.join(buf), 'abcd')
 
if __name__ == '__main__':
    unittest.main()