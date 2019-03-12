class Lcis:
    def findLengthOfLCIS(self, nums: 'List[int]') -> int:
        if not nums: return 0
        max_length, length, prev = 1, 1, nums[0]
        for cur in nums[1:]:
            if prev < cur:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
            prev = cur
        return max(max_length, length)
