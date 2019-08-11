class ArithmeticSequence:
    def longestArithSeqLength(self, A: 'List[int]') -> int:
        memo = [{} for _ in range(len(A))]
        max_len = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in memo[j]:
                    memo[i][diff] = 2
                else:
                    memo[i][diff] = 1 + memo[j][diff]
                max_len = max(max_len, memo[i][diff])
        return max_len