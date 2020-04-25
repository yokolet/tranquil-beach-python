import bisect

class RectangleSum:
    def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        for c1 in range(n):
            for c2 in range(c1, n):
                acc, memo = 0, [0]
                for r in range(m):
                    v = matrix[r][c1-1] if c1 > 0 else 0
                    acc += matrix[r][c2] - v
                    idx = bisect.bisect_left(memo, acc-k)
                    if idx < len(memo):
                        max_sum = max(max_sum, acc-memo[idx])
                    bisect.insort_left(memo, acc)
        return max_sum
