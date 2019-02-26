class MaxSubarraySumK:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_length, sum_sofar, memo = 0, 0, {0: -1} # {sum: index}
        for i in range(len(nums)):
            sum_sofar += nums[i]
            if sum_sofar - k in memo:
                max_length = max(max_length, i - memo[sum_sofar - k])
            if sum_sofar not in memo:
                memo[sum_sofar] = i
        return max_length
