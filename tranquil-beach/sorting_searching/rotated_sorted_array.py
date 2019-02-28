class RotatedSortedArray:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        def find_pivot(nums, left, right):
            if nums[left] < nums[right]: return right
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid
                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
 
        if not nums: return -1
        left, right = 0, len(nums) - 1
        if (left == right):
            return left if nums[left] == target else -1
        pivot = find_pivot(nums, left, right)
        if pivot != right:
            left, right = (0, pivot) if target > nums[right] else (pivot + 1, right)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1