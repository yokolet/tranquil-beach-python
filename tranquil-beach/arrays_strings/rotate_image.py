class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate2(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        low, high = 0, len(matrix)-1
        while low < high:
            for i in range(low, high):
                matrix[low][i], matrix[i][high] = matrix[i][high], matrix[low][i]
                matrix[low][i], matrix[high][high+low-i] = matrix[high][high+low-i], matrix[low][i]
                matrix[low][i], matrix[high+low-i][low] = matrix[high+low-i][low], matrix[low][i]
            low += 1
            high -= 1
