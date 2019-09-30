class MinJumpGame:
    def jump(self, nums: 'List[int]') -> int:
        if not nums or len(nums) < 2: return 0
        steps, cur, next = 0, 0, 0
        for i in range(len(nums)):
            if i > cur:
                steps += 1
                cur = next
            next = max(next, i+nums[i])
        return steps

    def jum1(self, nums: 'List[int]') -> int:
        n, steps, cur, idx, next = len(nums), 0, 0, 0, 0
        if n < 2: return 0
        while cur-idx+1 > 0:
            steps += 1
            while idx <= cur:
                next = max(next, idx+nums[idx])
                if next >= n-1: return steps
                idx += 1
            cur = next
        return 0

    def jump2(self, nums: 'List[int]') -> int:
        n = len(nums)
        steps = [n for i in range(n)]
        steps[-1] = 0
        for i in range(n-2, -1, -1):
            prev = i + 1
            for j in range(i, -1, -1):
                if j+nums[j] >= prev:
                    steps[j] = min(steps[j], steps[prev]+1)
        return steps[0]