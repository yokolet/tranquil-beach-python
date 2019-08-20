import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.friend_request import FriendRequest

class TestFriendRequest(unittest.TestCase):
    def setUp(self):
        self.func = FriendRequest().numFriendRequests

    def test_1(self):
        ages = [16,16]
        expected = 2
        self.assertEqual(expected, self.func(ages))

    def test_2(self):
        ages = [16,17,18]
        expected = 2
        self.assertEqual(expected, self.func(ages))

    def test_3(self):
        ages = [20,30,100,110,120]
        expected = 3
        self.assertEqual(expected, self.func(ages))

if __name__ == '__main__':
    unittest.main()