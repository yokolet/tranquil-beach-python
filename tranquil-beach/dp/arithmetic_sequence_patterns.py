from collections import defaultdict

class ArithmeticSequencePatterns:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> int:
        if len(A) < 3: return 0
        memo = [defaultdict(int) for _ in range(len(A))]
        result = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                result += memo[j][diff]
                memo[i][diff] += memo[j][diff] + 1
        return result