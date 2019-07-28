class SnakesLadders:
    def snakesAndLadders(self, board: 'List[List[int]]') -> int:
        n = len(board)
        goal = n * n
        def findRowCol(pos):
            q, r = divmod(pos-1, n)
            if q % 2 == 0:
                return n - 1 - q, r
            else:
                return n - 1 - q, n - 1 - r
    
        queue = [(1, 0)]
        visited = set([1])
        while queue:
            pos, step = queue.pop(0)
            r, c = findRowCol(pos)
            if board[r][c] != -1: pos = board[r][c]
            if pos == goal: return step
            for i in range(1, 7):
                tmp = pos + i
                if tmp <= goal and tmp not in visited:
                    visited.add(tmp)
                    queue.append((tmp, step + 1))
        return -1