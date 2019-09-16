from collections import defaultdict

class TwoArrays:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        memo, result = defaultdict(int), []
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        for v in nums1:
            memo[v] += 1
        for v in nums2:
            if v in memo and memo[v] > 0:
                result.append(v)
                memo[v] -= 1
        return result
        