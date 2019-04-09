import heapq

class KthLargest:
    def __init__(self, k: int, nums: 'List[int]'):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]