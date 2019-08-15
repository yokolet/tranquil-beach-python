from collections import defaultdict

class ThreeSum:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        memo = defaultdict(int)
        for v in nums:
            memo[v] += 1
        pos, neg = [], []
        for key in memo:
            if key > 0:
                pos.append(key)
            else:
                neg.append(key)
        result = []
        if 0 in memo and memo[0] >= 3:
            result.append([0, 0, 0])
        for a in neg:
            for b in pos:
                c = -(a + b)
                if c not in memo: continue
                if c > b:
                    result.append([a, b, c])
                elif c < a:
                    result.append([c, a, b])
                elif c in (a, b) and memo[c] > 1:
                    # c is a, or b, so the same value should exist more than 1
                    result.append([a, c, b])
        return result
        