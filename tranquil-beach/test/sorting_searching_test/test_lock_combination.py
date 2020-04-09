import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.lock_combination import LockCombination

class TestLockCombination(unittest.TestCase):
    def setUp(self):
        self.func = LockCombination().openLock

    def test_1(self):
        deadends, target = ["0201","0101","0102","1212","2002"], "0202"
        expected = 6
        self.assertEqual(expected, self.func(deadends, target))

    def test_2(self):
        deadends, target = ["8888"], "0009"
        expected = 1
        self.assertEqual(expected, self.func(deadends, target))

    def test_3(self):
        deadends, target = ["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"
        expected = -1
        self.assertEqual(expected, self.func(deadends, target))

    def test_4(self):
        deadends, target = ["0000"], "8888"
        expected = -1
        self.assertEqual(expected, self.func(deadends, target))

if __name__ == '__main__':
    unittest.main()
