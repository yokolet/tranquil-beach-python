class WordSearch:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, w):
            if not w: return True
            cur = board[i][j]
            board[i][j] = '#'
            if (i > 0 and board[i-1][j] == w[0] and dfs(i-1, j, w[1:])) \
                or (i < m-1 and board[i+1][j] == w[0] and dfs(i+1, j, w[1:])) \
                or (j > 0 and board[i][j-1] == w[0] and dfs(i, j-1, w[1:])) \
                or (j < n-1 and board[i][j+1] == w[0] and dfs(i, j+1, w[1:])):
                return True
            board[i][j] = cur

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, word[1:]):
                    return True
        return False
