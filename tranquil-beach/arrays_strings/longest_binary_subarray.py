class LongestBinarySubarray:
    def findMaxLength(self, nums: 'List[int]') -> int:
        max_len, count, diff = 0, 0, {0: -1}
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in diff:
                max_len = max(max_len, i - diff[count])
            else:
                diff[count] = i
        return max_len

    def findMaxLength2(self, nums: 'List[int]') -> int:
        max_len, zeros, ones, diff = 0, 0, 0, {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0: zeros += 1
            else: ones += 1
            d = ones - zeros
            if d in diff:
                max_len = max(max_len, i - diff[d])
            else:
                diff[d] = i
        return max_len
