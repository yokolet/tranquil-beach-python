import heapq

class KthLargest:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        queue = nums[:k]
        heapq.heapify(queue)
        for v in nums[k:]:
            if v > queue[0]:
                heapq.heapreplace(queue, v)
        return queue[0]