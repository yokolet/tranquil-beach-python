from collections import Counter

class Tasks:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks).most_common()
        maxCounts, sameCounts = counts[0][1], 0
        for _, v in counts:
            if v == maxCounts:
                sameCounts += 1
            else:
                break
        intervals = maxCounts * sameCounts
        intervals += (maxCounts - 1) * (n - (sameCounts - 1)) # between
        return max(len(tasks), intervals)

    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskCounts = Counter(tasks).values()
        maxValue = max(taskCounts)
        maxValueCount = list(taskCounts).count(maxValue)
        base = maxValue * maxValueCount
        base += (maxValue - 1) * (n - (maxValueCount - 1))
        return max(len(tasks), base)
