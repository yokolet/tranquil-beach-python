from collections import Counter

class Tasks:
    def leastInterval(self, tasks: 'List[str]', n: int) -> int:
        counts = Counter(tasks).most_common()
        max_counts, same_counts = counts[0][1], 0
        for _, v in counts:
            if v == max_counts:
                same_counts += 1
            else:
                break
        intervals = max_counts * same_counts
        intervals += (max_counts - 1) * (n - (same_counts - 1)) # between
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
