import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.interval import Interval
from sorting_searching.min_meeting_rooms import MinRooms

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.func = MinRooms()

    def test_1(self):
        arr = [[0, 30],[5, 10],[15, 20]]
        expected = 2
        intervals = [Interval(s, e) for [s, e] in arr]
        self.assertEqual(self.func.minMeetingRooms(intervals), expected)

    def test_2(self):
        arr =  [[7,10],[2,4]]
        expected = 1
        intervals = [Interval(s, e) for [s, e] in arr]
        self.assertEqual(self.func.minMeetingRooms(intervals), expected)

    def test_3(self):
        arr = [[2,11],[6,16],[11,16]]
        expected = 2
        intervals = [Interval(s, e) for [s, e] in arr]
        self.assertEqual(self.func.minMeetingRooms(intervals), expected)

if __name__ == '__main__':
    unittest.main()
