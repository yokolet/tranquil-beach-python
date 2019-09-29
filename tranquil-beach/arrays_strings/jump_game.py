class JumpGame:
    def canJump(self, nums: 'List[int]') -> bool:
        n = len(nums)
        prev = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= prev:
                prev = i
        return prev == 0

    def canJump2(self, nums: 'List[int]') -> bool:
        max_idx = 0
        for i in range(len(nums)):
            if i > max_idx: return False
            if max_idx >= len(nums): return True
            max_idx = max(max_idx, nums[i]+i)
        return True