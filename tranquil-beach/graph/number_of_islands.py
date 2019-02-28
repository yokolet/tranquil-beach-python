class NumberOfIslands:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0

        cols = len(grid[0])
        memo = [0 for _ in range(cols)]
        groups = [0]
        gno = 1
        for row in grid:
            for i in range(cols):
                if row[i] == '0':
                    memo[i] = 0
                    continue
                up = groups[memo[i]]
                tmp = 0 if i == 0 else memo[i - 1]
                left = groups[tmp]
                if up == 0 and left == 0:
                    memo[i] = gno
                    groups.append(gno)
                    gno += 1
                elif up == 0:
                    memo[i] = left
                elif left == 0:
                    memo[i] = up
                elif up > left:
                    groups[up] = left
                    memo[i] = left
                else:
                    # up < left
                    groups[left] = up
                    memo[i] = up
        count = 0
        for i in range(1, len(groups)):
            if i == groups[i]:
                count += 1
        return count