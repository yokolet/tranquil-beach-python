class ArithmeticSlice:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> int:
        if len(A) < 3: return 0
        memo = [0 for _ in range(len(A))]
        diff = A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                memo[i] = memo[i-1]+1
            else:
                diff = A[i] - A[i-1]
        return sum(memo)