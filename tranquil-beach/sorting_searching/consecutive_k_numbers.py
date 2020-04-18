from collections import defaultdict

class ConsecutiveKNumbers:
    def isPossibleDivide(self, nums: 'List[int]', k: int) -> bool:
        if len(nums) % k != 0: return False
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for v in sorted(counts):
            if counts[v] == 0: continue
            count = counts[v]
            for i in range(k):
                if v+i in counts and counts[v+i] - count >= 0:
                    counts[v+i] -= count
                else:
                    return False
        return True

    # fast, but has a flaw
    def isPossibleDivide2(self, nums: 'List[int]', k: int) -> bool:
        if len(nums) % k != 0: return False
        counts = defaultdict(int)
        for n in nums:
            counts[n%k] += 1
        return len(set(counts.values())) == 1
