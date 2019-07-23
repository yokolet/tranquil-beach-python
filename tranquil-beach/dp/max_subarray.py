class MaxSubarray:
    def maxSubArray(self, nums: 'List[int') -> int:
        max_sum = float('-inf')
        cur_sum = 0
        for v in nums:
            cur_sum = max(cur_sum + v, v)
            max_sum = max(max_sum, cur_sum)
        return max_sum
