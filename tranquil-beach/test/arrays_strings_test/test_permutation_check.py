import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.permutation_check import PermutationCheck

class TestPermutationCheck(unittest.TestCase):
    def setUp(self):
        self.func = PermutationCheck().checkInclusion

    def test_1(self):
        s1, s2 = 'ab', 'eidbaooo'
        expected = True
        self.assertTrue(self.func(s1, s2))

    def test_2(self):
        s1, s2 = 'ab', 'eidboaoo'
        expected = False
        self.assertFalse(self.func(s1, s2))

if __name__ == '__main__':
    unittest.main()