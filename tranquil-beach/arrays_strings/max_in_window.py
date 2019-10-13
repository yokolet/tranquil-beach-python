class MaxInWindow:
    def maxSlidingWindow(self, nums: 'List[int]', k: int) -> 'List[int]':
        if not nums: return []
        if k == len(nums): return [max(nums)]
        result = [max(nums[:k])]
        for i in range(k, len(nums)):
            if nums[i] > result[-1]:
                result.append(nums[i])
            else:
                if nums[i-k] == result[-1]:
                    result.append(max(nums[i-k+1:i+1]))
                else:
                    result.append(result[-1])
        return result

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def find_max(arr):
            max_v = float('-inf')
            max_idx = -1
            for idx, v in enumerate(arr):
                if v >= max_v:
                    max_v = v
                    max_idx = idx
            return max_idx, max_v
        if len(nums) == 0:
            return []
        maxsofar_idx, maxsofar_v = find_max(nums[:k])
        result = [maxsofar_v]
        for i in range(k, len(nums)):
            if nums[i] >= maxsofar_v:
                maxsofar_idx = i
                maxsofar_v = nums[i]
            elif maxsofar_idx <= i-k:
                maxsofar_idx, maxsofar_v = find_max(nums[i-k+1:i+1])
            result.append(maxsofar_v)
        return result