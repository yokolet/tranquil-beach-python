class SplitArray:
    def splitArray(self, nums: 'List[int]', m: int) -> int:
        low, high = max(max(nums), sum(nums)//m), sum(nums)
        while low < high:
            mid = (low + high) // 2
            g_sum = 0
            groups = 1
            for v in nums:
                g_sum += v
                if g_sum > mid:
                    g_sum = v
                    groups += 1
            if groups > m:
                low = mid + 1
            else:
                high = mid
        return low