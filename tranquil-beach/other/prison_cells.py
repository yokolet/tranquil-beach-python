class PrisonCells:
    def prisonAfterNDays(self, cells: 'List[int]', N: int) -> 'List[int]':
        patterns = {}
        while N > 0:
            c = tuple(cells)
            if c in patterns:
                N %= (patterns[c] - N)
            patterns[c] = N
            if N >= 1:
                N -= 1
                cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, 7)] + [0]
        return cells
