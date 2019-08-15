class Perimeter:
    def islandPerimeter(self, grid: 'List[List[int]]') -> int:
        result, m, n = 0, len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        return result

    def islandPerimeter2(self, grid: 'List[List[int]]') -> int:
        result, m, n = 0, len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        result += 1
                    if r == m-1 or grid[r+1][c] == 0:
                        result += 1
                    if c == 0 or grid[r][c-1] == 0:
                        result += 1
                    if c == n-1 or grid[r][c+1] == 0:
                        result += 1
        return result
