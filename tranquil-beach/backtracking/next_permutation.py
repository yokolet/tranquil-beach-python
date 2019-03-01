class NextPermutation:
    def nextPermutation(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]: break
            i -= 1
        if i == -1:
            nums[:] = nums[::-1]
        else:
            succ = n - 1
            while nums[succ] <= nums[i]:
                succ -= 1
            nums[i], nums[succ] = nums[succ], nums[i]
            nums[i+1:] = nums[i+1:][::-1]