class GameOfLife:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def calc(i, j):
            neighbors = [
                [i-1, j-1],[i-1,j],[i-1,j+1],
                [i, j-1],[i,j+1],
                [i+1, j-1],[i+1, j],[i+1,j+1]
            ]
            sum = 0
            for r,c in neighbors:
                if 0 <= r < m and 0 <= c < n:
                    sum += (board[r][c] & 1)
            return sum
        for i in range(m):
            for j in range(n):
                status = calc(i, j)
                if board[i][j] == 1 and (status == 2 or status == 3):
                    board[i][j] = 3
                else:
                    if status == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1