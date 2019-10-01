class MissingRanges:
    def findMissingRanges(self, nums: 'List[int]', lower: int, upper: int) -> 'List[str]':
        nums = [lower-1] + nums + [upper+1]
        result = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                result.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                result.append('{}->{}'.format(nums[i-1]+1, nums[i]-1))
        return result

    def findMissingRanges2(self, nums: 'List[int]', lower: int, upper: int) -> 'List[str]':
        result = []
        if not nums:
            if lower == upper: return [str(upper)]
            else: return ['{}->{}'.format(lower, upper)]
        if nums[0] > lower:
            if nums[0]-lower == 1: result.append(str(lower))
            else: result.append('{}->{}'.format(lower, nums[0]-1))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                result.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
                result.append('{}->{}'.format(nums[i-1]+1, nums[i]-1))
        if nums[-1] < upper:
            if upper - nums[-1] == 1: result.append(str(upper))
            else: result.append('{}->{}'.format(nums[-1]+1, upper))
        return result