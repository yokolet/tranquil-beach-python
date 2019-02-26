class MoveZeros:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def moveZeroes4(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i, v in enumerate(nums):
            if v == 0:
                zeros += 1
            else:
                nums[i - zeros] = v
        for i in range(1, zeros + 1):
            nums[-i] = 0


    def moveZeroes2(self, nums: 'List[int]') -> 'None':
        zero_count = 0
        for index, value in enumerate(nums):
            if value == 0:
                zero_count += 1
            else:
                nums[index - zero_count] = value

        while zero_count != 0:
            nums[len(nums) - zero_count] = 0
            zero_count -= 1

    def moveZeroes3(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        t = (item for item in nums if item != 0)
        c = nums.count(0)
        nums[:] = list(t) + [0]*c

    def moveZeroesSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)
        while start < end:
            if nums[start] == 0:
                nums.append(nums.pop(start))
                end -= 1
            else:
                start += 1