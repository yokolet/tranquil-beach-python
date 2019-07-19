class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                memo[j] += memo[j-1]
        return memo[-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            memo[i][0] = 1
        for i in range(n):
            memo[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[m-1][n-1]