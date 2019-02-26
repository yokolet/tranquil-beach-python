import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.add_binary import AddBinary

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.func = AddBinary()

    def test_1(self):
        a = "11"
        b = "1"
        expected = "100"
        self.assertEqual(self.func.addBinary(a, b), expected)

if __name__ == '__main__':
    unittest.main()