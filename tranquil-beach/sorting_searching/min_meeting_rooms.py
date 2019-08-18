import heapq

class MinRooms:
    def minMeetingRooms(self, intervals: 'List[List[int]]') -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        i, j = 0, 0
        result, count = 0, 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                count += 1
                i +=1
                result = max(result, count)
            else:
                count -=1
                j +=1
        return result

    def minMeetingRooms2(self, intervals: 'List[List[int]]') -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        heap = [intervals[0][1]]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] < heap[0]:
                count += 1
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappushpop(heap, intervals[i][1])
        return count
