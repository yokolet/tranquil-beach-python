import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from other.exclusive_time import ExclusiveTime

class TestExclusiveTime(unittest.TestCase):
    def setUp(self):
        self.func = ExclusiveTime()

    def test_1(self):
        n = 2
        logs = [
            "0:start:0",
            "1:start:2",
            "1:end:5",
            "0:end:6"
            ]
        expected = [3, 4]
        self.assertEqual(self.func.exclusiveTime(n, logs), expected)

if __name__ == '__main__':
    unittest.main()