class NearestGate:
    def wallsAndGates(self, rooms: 'List[List[int]]') -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return
        m, n = len(rooms), len(rooms[0])
        def bfs(row, col):
            queue = [
                (row-1, col, 1),
                (row, col-1, 1),
                (row, col+1, 1),
                (row+1, col, 1)
            ]
            while queue:
                r, c, v = queue.pop(0)
                if 0 <= r < m and 0 <= c< n and rooms[r][c] > v:
                    rooms[r][c] = v
                    queue.append((r-1, c, v+1))
                    queue.append((r, c-1, v+1))
                    queue.append((r, c+1, v+1))
                    queue.append((r+1, c, v+1))

        for row in range(m):
            for col in range(n):
                if rooms[row][col] != 0: continue
                bfs(row, col)
