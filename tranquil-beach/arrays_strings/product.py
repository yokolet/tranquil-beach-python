class Product:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        acc, result = 1, []
        for n in nums:
            result.append(acc)
            acc *= n
        acc = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= acc
            acc *= nums[i]
        return result