class SpiralMatrix:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or not matrix[0]: return []
        m, n, result = len(matrix), len(matrix[0]), []
        row_start, row_end, col_start, col_end = 0, m-1, 0, n-1
        count = m * n
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end+1):
                result.append(matrix[row_start][i])
                count -= 1
            if count == 0: break
            row_start += 1
            for i in range(row_start, row_end+1):
                result.append(matrix[i][col_end])
                count -= 1
            if count == 0: break
            col_end -= 1
            for i in range(col_end, col_start-1, -1):
                result.append(matrix[row_end][i])
                count -= 1
            if count == 0: break
            row_end -= 1
            for i in range(row_end, row_start-1, -1):
                result.append(matrix[i][col_start])
                count -= 1
            if count == 0: break
            col_start += 1
        return result

    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        startRow, endRow = 0, m-1
        startCol, endCol = 0, n-1
        result = []
        count = m * n
        while startRow <= endRow and startCol <= endCol:
            for i in range(startCol, endCol+1):
                result.append(matrix[startRow][i])
                count -= 1
            if count == 0: break
            startRow += 1
            for i in range(startRow, endRow+1):
                result.append(matrix[i][endCol])
                count -= 1
            if count == 0: break
            endCol -= 1
            for i in range(endCol, startCol-1, -1):
                result.append(matrix[endRow][i])
                count -= 1
            if count == 0: break
            endRow -= 1
            for i in range(endRow, startRow-1, -1):
                result.append(matrix[i][startCol])
                count -= 1
            if count == 0: break
            startCol += 1
        return result
