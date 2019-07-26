import heapq

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.maxheap = [] # smaller values than median
        self.minheap = [] # bigger values than median

    def addNum(self, num: int):
        if len(self.maxheap) == len(self.minheap):
            heapq.heappush(self.minheap,
                           -heapq.heappushpop(self.maxheap, -num))
        else:
            heapq.heappush(self.maxheap,
                           -heapq.heappushpop(self.minheap, num))
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2.0

    