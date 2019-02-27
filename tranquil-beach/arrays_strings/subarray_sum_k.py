from collections import defaultdict

class SubarraySumK:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        count, acc, memo = 0, 0, {0: 1}
        for v in nums:
            acc += v
            if acc - k in memo:
                count += memo[acc - k]
            if acc in memo:
                memo[acc] += 1
            else:
                memo[acc] = 1
        return count

    def subarraySum1(self, nums: 'List[int]', k: int) -> int:
        count, acc, memo = 0, 0, defaultdict(int)
        for v in nums:
            acc += v
            if acc == k: count += 1
            count += memo[acc - k]
            memo[acc] += 1
        return count
