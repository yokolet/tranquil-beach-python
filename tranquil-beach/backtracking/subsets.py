from functools import reduce

class Subsets:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda acc, x: acc + [y + [x] for y in acc], nums, [[]])