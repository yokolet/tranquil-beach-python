class MinSubarraySum:
    def minSubArrayLen(self, s: int, nums: 'List[int]') -> int:
        n = len(nums)
        if n == 0 or (n == 1 and nums[0] < s): return 0
        acc, left, min_len = 0, 0, n + 1
        for i in range(n):
            acc += nums[i]
            while acc >= s:
                min_len = min(min_len, i - left + 1)
                acc -= nums[left]
                left += 1
        return min_len if min_len <= n else 0


    def minSubArrayLenSlow(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or (n == 1 and nums[0] < s):
            return 0
        if nums[0] >= s:
            return 1
        sum_sofar = nums[0]
        start = 0
        min_start, min_end = 0, 0
        for end in range(1, n):
            sum_sofar += nums[end]
            if sum_sofar >= s:
                while start < end and sum_sofar - nums[start] >= s:
                    sum_sofar -= nums[start]
                    start += 1
                if min_end == 0 or end - start < min_end - min_start:
                    min_start, min_end = start, end
        if min_start == 0 and min_end == 0:
            return 0
        else:
            return min_end - min_start + 1