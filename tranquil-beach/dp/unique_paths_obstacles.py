class UniquePathsObstacles:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [0 for _ in range(n)]
        if obstacleGrid[0][0] == 0: memo[0] = 1
        for i in range(m):
            if obstacleGrid[i][0]: memo[0] = 0
            for j in range(1, n):
                memo[j] = memo[j-1] + memo[j] if obstacleGrid[i][j] == 0 else 0
        return memo[-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: 'List[List[int]]') -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0: memo[0][0] = 1
        for i in range(1, m):
            memo[i][0] = memo[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for i in range(1, n):
            memo[0][i] = memo[0][i-1] if obstacleGrid[0][i] == 0 else 0
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] += memo[i-1][j] + memo[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return memo[m-1][n-1]