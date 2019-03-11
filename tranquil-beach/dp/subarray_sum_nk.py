class SubarraySumNK:
    def checkSubarraySum(self, nums: 'List[int]', k: int) -> bool:
        sum, memo = 0, {0: -1}
        for i in range(len(nums)):
            if k != 0:
                sum = (sum + nums[i]) % k
            else:
                sum += nums[i]
            if sum in memo:
                if i - memo[sum] >= 2: return True
            else:
                memo[sum] = i
        return False
