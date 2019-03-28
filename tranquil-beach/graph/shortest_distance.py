class ShortestDistance:
    def shortestDistance(self, grid: 'List[List[int]]') -> int:
        if not grid or not grid[0]: return -1
        m, n = len(grid), len(grid[0])
        dists, reached = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        counts = sum(x for row in grid for x in row if x == 1)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 1:
                    continue
                cnt, visited = 1, [[False]*n for _ in range(m)]
                queue = [(row, col, 0)]
                visited[row][col] = True
                while queue:
                    r, c, d = queue.pop(0)
                    reached[r][c] += 1
                    for i, j in ((r-1, c), (r, c-1), (r, c+1), (r+1, c)):
                        if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                            visited[i][j] = True
                            if grid[i][j] == 1:
                                cnt += 1
                            elif grid[i][j] == 0:
                                dists[i][j] += (d + 1)
                                queue.append((i, j, d+1))
                if counts != cnt: return -1
        
        return min([dists[i][j] for i in range(m) for j in range(n) if reached[i][j] == counts and grid[i][j] == 0] or [-1])
