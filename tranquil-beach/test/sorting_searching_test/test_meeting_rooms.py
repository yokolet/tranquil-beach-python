import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from sorting_searching.meeting_rooms import MeetingRooms

class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.func = MeetingRooms().canAttendMeetings

    def test_1(self):
        intervals = [[0,30],[5,10],[15,20]]
        self.assertFalse(self.func(intervals))

    def test_2(self):
        intervals = [[7,10],[2,4]]
        self.assertTrue(self.func(intervals))

if __name__ == '__main__':
    unittest.main()