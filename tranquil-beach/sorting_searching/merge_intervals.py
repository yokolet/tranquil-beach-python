from .interval import Interval

class MergeIntervals:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        result = []
        for i in intervals:
            if not result or result[-1].end < i.start:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
        return result