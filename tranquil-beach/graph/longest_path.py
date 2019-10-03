from collections import defaultdict

class LongestPath:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> int:
        if not matrix or not matrix[0]: return 0
        n, m = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(r, c):
            if memo[r][c] != -1: return memo[r][c]
            max_p = 0
            for i,j in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                if 0 <= i < n and 0 <= j < m and matrix[r][c] > matrix[i][j]:
                    max_p = max(max_p, dfs(i, j))
            memo[r][c] = max_p + 1
            return memo[r][c]

        max_path = 0
        for r in range(n):
            for c in range(m):
                max_path = max(max_path, dfs(r, c))
        return max_path

    def longestIncreasingPath2(self, matrix: 'List[List[int]]') -> int:
        if not matrix or not matrix[0]: return 0
        graph, start, n, m = {}, [], len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                graph[(r,c)] = []
                min_v = matrix[r][c]
                for i,j in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                    if 0 <= i < n and 0 <= j < m:
                        if matrix[r][c] < matrix[i][j]:
                            graph[(r, c)].append((i, j))
                        else:
                            min_v = min(min_v, matrix[i][j])
                if min_v == matrix[r][c]:
                    start.append((r, c))
        
        def dfs(r, c):
            if not graph[(r, c)]: return 1
            paths = []
            for i, j in graph[(r, c)]:
                paths.append(dfs(i, j))
            return max(paths)+1

        max_path = 0
        for r, c in start:
            max_path = max(max_path, dfs(r, c))
        return max_path
