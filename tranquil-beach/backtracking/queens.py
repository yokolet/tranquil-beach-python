class Queens:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        rows, cols, diag_1, diag_2, = set(), set(), set(), set()
        queens, result = [], []

        def placeQueens():
            if len(queens) == n:
                # base case, all queens could be placed
                board = [['.' for i in range(n)] for j in range(n)]
                for r, c in enumerate(queens):
                    board[r][c] = 'Q'
                result.append([''.join(row) for row in board])

            # row r will be saved in index r
            r = len(queens)
            for c in range(n):
                if r not in rows and c not in cols and\
                    r+c not in diag_1 and r+n-1-c not in diag_2:
                    rows.add(r)
                    cols.add(c)
                    diag_1.add(r+c)
                    diag_2.add(r+n-1-c)
                    queens.append(c)
                    placeQueens()
                    queens.pop()
                    diag_2.remove(r+n-1-c)
                    diag_1.remove(r+c)
                    cols.remove(c)
                    rows.remove(r)
        placeQueens()
        return result

    def solveNQueens2(self, n: int) -> 'List[List[str]]':
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def isValid(row, col):
            # check this row on the left
            for i in range(col):
                if board[row][i] == 'Q': return False
            # check upper diagonal
            for i, j in zip(range(row, -1 ,-1), range(col, -1, -1)):
                if board[i][j] == 'Q': return False
            # check lower diagonal
            for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == 'Q': return False
            return True

        def placeQueen(col):
            # base case, all queens could be placed
            if col == n:
                result.append([''.join(row) for row in board])
            for i in range(n):
                if isValid(i, col):
                    board[i][col] = 'Q'
                    placeQueen(col+1)
                    board[i][col] = '.'

        placeQueen(0)
        return result
