class MinPath:
    def minPathSum(self, grid: 'List[List[int]]') -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

    def minPathSum2(self, grid: 'List[List[int]]') -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        memo = [grid[0][0]]
        for v in grid[0][1:]:
            memo.append(memo[-1]+v)
        for i in range(1, m):
            memo[0] += grid[i][0]
            for j in range(1, n):
                memo[j] = min(memo[j-1], memo[j]) + grid[i][j]
        return memo[n-1]
