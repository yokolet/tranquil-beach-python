class Lcis:
    def findLengthOfLCIS(self, nums: 'List[int]') -> int:
        if not nums: return 0
        max_len, length, prev = 1, 1, nums[0]
        for cur in nums[1:]:
            if prev < cur:
                length += 1
            else:
                max_len = max(max_len, length)
                length = 1
            prev = cur
        return max(max_len, length)
