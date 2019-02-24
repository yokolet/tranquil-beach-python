class LIS:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums: return 0
        memo = [0] * len(nums)
        max_length = 0
        for i in range(len(nums)):
            left, right = 0, max_length
            while left < right:
                mid = (left + right) // 2
                if memo[mid] < nums[i]:
                    left = mid + 1
                else:
                    right  = mid
            memo[left] = nums[i]
            max_length = max(max_length, left + 1)
        return max_length


    # O(n^2) - very slow
    def lengthOfLIS_slow(self, nums: 'List[int]') -> 'int':
        if not nums: return 0
        memo = [1]*(len(nums))
        max_length = 1
        for i in range(1, len(nums)):
            j = 0
            while j < i:
                if nums[i] > nums[j] and memo[i] < memo[j] + 1:
                    memo[i] = memo[j] + 1
                    max_length = max(max_length, memo[i])
                j += 1
        return max_length
    
    def lengthOfLIS3(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        arr = [0]*len(nums)
        size = 0
        for ele in nums:
            i, j = 0, size
            while i != j:
                m = (i+j)//2
                if arr[m] < ele:
                    i = m+1
                else:
                    j = m
            
            size = max(size, i+1)
            arr[i] = ele
            
        return size

    def lengthOfLIS2(self, nums: 'List[int]') -> 'int':
        def CeilIndex(nums, l, r, key):
            while (r - l > 1):
                m = l + (r - l)//2
                if (nums[m] >= key):
                    r = m
                else:
                    l = m
            return r

        size = len(nums)
        if size == 0:
            return 0
        tailTable = [0 for i in range(size)]
        length = 0 # always points empty slot

        tailTable[0] = nums[0]
        length = 1
        for i in range(1, size):
            if (nums[i] < tailTable[0]):
                # new smallest value
                tailTable[0] = nums[i]
            elif (nums[i] > tailTable[length-1]):
                # nums[i] wants to extend
                # largest subsequence
                tailTable[length] = nums[i]
                length += 1
            else: 
                # nums[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace 
                # ceil value in tailTable
                tailTable[CeilIndex(tailTable, -1, length-1, nums[i])] = nums[i]
        return length
