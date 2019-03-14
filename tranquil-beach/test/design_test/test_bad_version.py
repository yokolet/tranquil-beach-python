import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from unittest.mock import Mock, patch
from design.version import isBadVersion
from design.bad_version import BadVersion

class TestBadVersion(unittest.TestCase):
    def setUp(self):
        self.func = BadVersion(lambda x: True if x >= 4 else False)

    def test_1(self):
        n = 5
        expected = 4
        self.assertEqual(self.func.firstBadVersion(n), expected)


if __name__ == '__main__':
    unittest.main()