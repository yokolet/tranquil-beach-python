class MaxProduct:
    def maxProduct(self, nums: 'List[int]') -> int:
        cur_min, cur_max, max_prod = nums[0], nums[0], nums[0]
        for v in nums[1:]:
            cur_min, cur_max = min(cur_min*v, cur_max*v, v), max(cur_min*v, cur_max*v, v)
            max_prod = max(max_prod, cur_max)
        return max_prod