import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.min_meeting_rooms import MinRooms

class TestMinRooms(unittest.TestCase):
    def setUp(self):
        self.func = MinRooms().minMeetingRooms

    def test_1(self):
        intervals = [[0, 30],[5, 10],[15, 20]]
        expected = 2
        self.assertEqual(self.func(intervals), expected)

    def test_2(self):
        intervals =  [[7,10],[2,4]]
        expected = 1
        self.assertEqual(self.func(intervals), expected)

    def test_3(self):
        intervals = [[2,11],[6,16],[11,16]]
        expected = 2
        self.assertEqual(self.func(intervals), expected)

if __name__ == '__main__':
    unittest.main()
