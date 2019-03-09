import heapq
from collections import defaultdict

class Range:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        all_nums = defaultdict(set)
        for i, num in enumerate(nums):
            for v in num:
                all_nums[v].add(i)
        all_nums = sorted(all_nums.items())
        min_range, min_diff = [all_nums[0][0], all_nums[-1][0]], all_nums[-1][0] - all_nums[0][0]
        start, missing, memo = 0, len(nums), defaultdict(int)
        for v, ks in all_nums:
            for k in ks:
                if k not in memo or memo[k] <= 0:
                    missing -= 1
                memo[k] += 1
            while missing <= 0 and all_nums[start][0] <= v:
                if v - all_nums[start][0] < min_diff:
                    min_range = [all_nums[start][0], v]
                    min_diff = v - all_nums[start][0]
                for k in all_nums[start][1]:
                    memo[k] -= 1
                    if memo[k] <= 0:
                        missing += 1
                start += 1
        return min_range

    def smallestRange3(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        queue = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(queue)
        max_val = max(queue, key=lambda x: x[0])[0]
        min_range = [float('-inf'), float('inf')]
        while queue:
            min_val, i, j = heapq.heappop(queue)
            if max_val - min_val < min_range[1] - min_range[0]:
                min_range = [min_val, max_val]
            if j + 1 == len(nums[i]):
                return min_range
            v = nums[i][j + 1]
            max_val = max(max_val, v)
            heapq.heappush(queue, (v, i, j + 1))

    def smallestRange2(self, nums: 'List[List[int]]') -> 'List[int]':
        vals = defaultdict(set)
        for i, num in enumerate(nums):
            for val in num:
                vals[val].add(i)
        vals = sorted(vals.items())
        ans = [vals[0][0], vals[-1][0]]

        need, count = len(nums), defaultdict(int)
        h = 0
        for val, arrs in vals:
            for arr in arrs:
                if arr not in count or not count[arr]:
                    need -= 1
                count[arr] += 1
            while need <= 0 and vals[h][0] <= val:
                if val - vals[h][0] < ans[1] - ans[0]:
                    ans = [vals[h][0], val]
                for arr in vals[h][1]:
                    count[arr] -= 1
                    if count[arr] <= 0:
                        need += 1
                h = h + 1

        return ans