import random
import bisect

class RandomPick:
    def __init__(self, w: 'List[int]'):
        total = sum(w)
        pvalues = [x/total for x in w]
        psums = [pvalues[0]]
        for p in pvalues[1:]:
            psums.append(p + psums[-1])
        psums[-1] = 1 
        self.psums = psums 

    def pickIndex(self) -> int:
        pick = random.random()
        left, right = 0, len(self.psums) - 1
        while left < right:
            mid = (left + right) // 2
            if pick >= self.psums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def pickIndex3(self) -> int:
        rand = random.random()
        index = bisect.bisect_left(self.psums,rand)
        return index

    def __init__2(self, w: 'List[int]'):
        self.acc_sum = []
        self.sum_sofar = 0
        for v in w:
            self.sum_sofar += v
            self.acc_sum.append(self.sum_sofar)
    
    def pickIndex2(self) -> int:
        pick = random.uniform(0.0, self.acc_sum[-1])
        left, right = 0, len(self.acc_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if pick >= self.acc_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left
