class MergeIntervals:
    def merge(self, intervals: 'List[List[int]]') -> 'List[List[int]]':
        if len(intervals) < 2: return intervals
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for value in intervals[1:]:
            if result[-1][1] < value[0]:
                result.append(value)
            elif result[-1][1] < value[1]:
                result[-1][1] = value[1]
        return result
