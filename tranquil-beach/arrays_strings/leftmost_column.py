class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]
    
    def dimensions(self) -> 'List[int]':
        return [len(self.matrix), len(self.matrix[0])]

class LeftmostColumn:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def search(r, h):
            low, high = 0, h
            while low < high:
                mid = (low + high) // 2
                if binaryMatrix.get(r, mid) == 1:
                    if mid >= 1 and binaryMatrix.get(r, mid-1) == 0:
                        return mid
                    else:
                        high = mid-1
                else:
                    low = mid+1
            return high

        rows, cols = binaryMatrix.dimensions()
        idx = float('inf')
        high = cols-1
        for i in range(rows):
            if binaryMatrix.get(i, high) == 0: continue
            if binaryMatrix.get(i, 0) == 1: return 0
            idx = min(idx, search(i, high))
            high = idx-1
        return -1 if idx == float('inf') else idx
