class Maze:
    def hasPath(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> bool:
        if not maze or not maze[0]: return False
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        queue = [start]
        visited[start[0]][start[1]] = True
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while queue:
            cur_r, cur_c = queue.pop(0)
            if cur_r == destination[0] and cur_c == destination[1]: return True
            for r, c in dirs:
                i, j = cur_r + r, cur_c + c
                while 0 <= i < m and 0 <= j < n and maze[i][j] == 0:
                    i += r
                    j += c
                i -= r
                j -= c
                if not visited[i][j]:
                    queue.append([i, j])
                    visited[i][j] = True
        return False
