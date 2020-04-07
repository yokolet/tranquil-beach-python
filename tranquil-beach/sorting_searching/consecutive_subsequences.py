from collections import defaultdict

class ConsecutiveSubsequences:
    def isPossible(self, nums: 'List[int]') -> bool:
        num_dict = defaultdict(int)
        for i in range(len(nums)):
            num_dict[nums[i]] += 1
        last_dict = defaultdict(int)
        for num in nums:
            if last_dict[num-1]:
                last_dict[num-1] -= 1
            elif num_dict[num+1] and num_dict[num+2]:
                num_dict[num+1] -= 1
                num_dict[num+2] -= 1
            else:
                return False
            last_dict[num] += 1
        return True