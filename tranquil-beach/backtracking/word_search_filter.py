class WordSearchFilter:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        m, n = len(board), len(board[0])
        result = set()
        def buildTrie():
            root = {}
            for word in words:
                cur = root
                for c in word:
                    if c not in cur:
                        cur[c] = {}
                    cur = cur[c]
                cur['$'] = {}
            return root

        def dfs(i, j, w, cur):
            if '$' in cur: result.add(w)
            if i < 0 or i == m or j < 0 or j == n: return
            if board[i][j] not in cur: return
            c = board[i][j]
            board[i][j] = '#'
            dfs(i-1, j, w+c, cur[c])
            dfs(i+1, j, w+c, cur[c])
            dfs(i, j-1, w+c, cur[c])
            dfs(i, j+1, w+c, cur[c])
            board[i][j] = c
        
        root = buildTrie()
        for i in range(m):
            for j in range(n):
                dfs(i, j, '', root)
        return list(result)
