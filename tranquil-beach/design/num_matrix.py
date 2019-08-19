class NumMatrix:
    def __init__(self, matrix: 'List[List[int]]'):
        def sum_matrix():
            m, n = len(matrix), len(matrix[0]) if matrix else 0
            result = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    result[i + 1][j + 1] = result[i][j + 1] + result[i + 1][j] - result[i][j] + matrix[i][j]
            return result
        self.acc_sum = sum_matrix()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.acc_sum[row2+1][col2+1]
        result -= self.acc_sum[row1][col2+1] # upper
        result -= self.acc_sum[row2+1][col1] # left
        result += self.acc_sum[row1][col1]   # adds doubly subtracted area
        return result
