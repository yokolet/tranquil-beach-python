import heapq
from .interval import Interval

import heapq

class MinRooms:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        i, j = 0, 0
        result = 0
        current = 0
        while i < len(intervals):
            if starts[i] < ends[j]:
                current += 1
                i +=1
                result = max(result, current)
            else:
                current -=1
                j +=1
        return result

    def minMeetingRooms4(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]:
                count += 1
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappushpop(heap, intervals[i].end)
        return count

    def minMeetingRooms2(self, intervals: 'List[Interval]') -> 'int':
        if (not intervals): return 0
        intervals = sorted(intervals, key = lambda a: a.end)
        count = 1
        max_count = 1
        min_end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= intervals[i-1].end:
                count = 1
                min_end = intervals[i].end
            if (intervals[i].start < intervals[i-1].end or
                intervals[i].start < intervals[i-1].start):
                if min_end > intervals[i].start:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    min_end = intervals[i-1].end
        return max_count

    

        # slow
        def minMeetingRooms3(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: int
            """
            intervals.sort(key=lambda x: x.start)
            heap = []
            for cur in intervals:
                if heap and heap[0] <= cur.start:
                    heapq.heapreplace(heap, cur.end)
                else:
                    heapq.heappush(heap, cur.end)
            return len(heap)