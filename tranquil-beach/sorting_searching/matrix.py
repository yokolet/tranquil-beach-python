class Matrix:
    def searchMatrix2(self, matrix: 'List[List[int]]', target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                if c >= 0 and matrix[r][c-1] < target:
                    return False
                c -= 1
            else:
                r += 1
        return False

    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid//n][mid%n] >= target:
                right = mid
            else:
                left = mid 
        if matrix[left//n][left%n] == target or\
            matrix[right//n][right%n] == target:
            return True
        return False