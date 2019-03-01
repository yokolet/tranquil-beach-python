class PermutationsWithDup:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        done = False
        result = []
        nums.sort()
        while not done:
            result.append(nums[:])
            i = n - 2
            while i >= 0:
                if nums[i] < nums[i + 1]: break
                i -= 1
            if i == -1: done = True
            else:
                succ = n - 1
                while nums[succ] <= nums[i]:
                    succ -= 1
                nums[i], nums[succ] = nums[succ], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
        return result

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_(arr, path, result):
            if not arr:
                result.append(path)
            else:
                for i in range(len(arr)):
                    if i > 0 and arr[i] == arr[i - 1]:
                        continue
                    permute_(arr[:i]+arr[i+1:], path+arr[i:i+1], result)
        result = []
        permute_(sorted(nums), [], result)
        return result

    def permuteUnique3(self, nums: 'List[int]') -> 'List[List[int]]':
        import functools
        return functools.reduce(lambda result, num: [[*permutation[:_], num, *permutation[_:]] for permutation in result for _ in range([*permutation, num].index(num) + 1)], nums, [[]])