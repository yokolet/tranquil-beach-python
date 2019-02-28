from itertools import permutations

class Permutations:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(x) for x in permutations(nums)]

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_(arr, path, result):
            if not arr:
                result.append(path)
            for i in range(len(arr)):
                permute_(arr[0:i]+arr[i+1:], path+[arr[i]], result)
        result = []
        permute_(nums, [], result)
        return result