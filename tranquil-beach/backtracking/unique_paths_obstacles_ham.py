class UniquePathsObstaclesHam:
    def uniquePathsIII(self, grid: 'List[List[int]]') -> int:
        m, n = len(grid), len(grid[0])
        def findCountAndStart():
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0: count += 1
                    if grid[i][j] == 1:
                        start = i, j
            return count, start

        def dsf(count, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                return 1 if count == 0 else 0
            result = 0
            grid[i][j] = -1
            for nx, ny in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                result += dsf(count - 1, i + nx, j + ny)
            grid[i][j] = 0
            return result

        count, (start_i, start_j) = findCountAndStart()
        return dsf(count+1, start_i, start_j)

    def uniquePathsIII2(self, grid: 'List[List[int]]') -> int:
        I, J = len(grid)-1, len(grid[0])-1

        def find_s():
            n_zeros = 0
            for i, r in enumerate(grid):
                for j, v in enumerate(r):
                    if v == 0: n_zeros += 1
                    elif v == 1: start = i, j
            return start, n_zeros

        def search(i, j, d):
            c = grid[i][j]
            if c == 2:
                return 1 if d == -1 else 0
            grid[i][j] = -1
            ans = 0
            d -= 1
            if i > 0 and grid[i-1][j] != -1: ans += search(i-1, j, d)
            if i < I and grid[i+1][j] != -1: ans += search(i+1, j, d)
            if j > 0 and grid[i][j-1] != -1: ans += search(i, j-1, d)
            if j < J and grid[i][j+1] != -1: ans += search(i, j+1, d)
            grid[i][j] = c
            return ans

        (i, j), n_zeros = find_s()
        grid[i][j] = -1
        ans = 0
        d = n_zeros-1
        if i > 0 and grid[i-1][j] != -1: ans += search(i-1, j, d)
        if i < I and grid[i+1][j] != -1: ans += search(i+1, j, d)
        if j > 0 and grid[i][j-1] != -1: ans += search(i, j-1, d)
        if j < J and grid[i][j+1] != -1: ans += search(i, j+1, d)
        return ans