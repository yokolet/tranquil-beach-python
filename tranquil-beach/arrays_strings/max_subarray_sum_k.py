class MaxSubarraySumK:
    def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
        max_len, acc, memo = 0, 0, {0: -1} # {sum: index}
        for i in range(len(nums)):
            acc += nums[i]
            if acc - k in memo:
                max_len = max(max_len, i - memo[acc - k])
            if acc not in memo:
                memo[acc] = i
        return max_len
