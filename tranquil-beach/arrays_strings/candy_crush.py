class CandyCrush:
    def candyCrush(self, board: 'List[List[int]]') -> 'List[List[int]]':
        def search(b, row, col):
            # down
            if row < rows-2 and b[row+1][col] == b[row][col] and b[row+2][col] == b[row][col]:
                counts[col].add(row)
                counts[col].add(row+1)
                counts[col].add(row+2)
                i = row + 3
                while i < rows and b[i][col] == b[row][col]:
                    counts[col].add(i)
                    i += 1          
            # right
            if col < cols-2 and b[row][col+1] == b[row][col] and b[row][col+2] == b[row][col]:
                counts[col].add(row)
                counts[col+1].add(row)
                counts[col+2].add(row)
                j = col + 3
                while j < cols and b[row][j] == b[row][col]:
                    counts[j].add(row)
                    j += 1
        
        def update():
            for c in range(cols):
                i = rows-1
                for r in range(rows-1, -1, -1):
                    if r not in counts[c]:
                        board[i][c] = board[r][c]
                        i -= 1
                while i >= 0:
                    board[i][c] = 0
                    i -= 1

        rows, cols= len(board), len(board[0])
        while True:
            counts = [set() for _ in range(cols)]
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 0: continue
                    search(board, r, c)
            if sum([len(c) for c in counts]) == 0: break
            update()
        return board
