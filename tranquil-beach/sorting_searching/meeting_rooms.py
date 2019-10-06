class MeetingRooms:
    def canAttendMeetings(self, intervals: 'List[List[int]]') -> bool:
        intervals.sort(key=lambda x: x[0])
        prev_e = -1
        for cur_s, cur_e in intervals:
            if prev_e > cur_s: return False
            prev_e = cur_e
        return True