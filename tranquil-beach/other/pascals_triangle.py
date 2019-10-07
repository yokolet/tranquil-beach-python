class PascalsTriangle:
    def generate(self, numRows: int) -> 'List[List[int]]':
        result = []
        for line in range(1, numRows+1):
            C = 1
            sub = []
            for i in range(1, line+1):
                sub.append(C)
                C = int(C * (line - i) / i)
            result.append(sub)
        return result

    def generate2(self, numRows: int) -> 'List[List[int]]':
        if numRows == 0: return None
        for i in range(numRows):
            if i < 1:
                result = [[1]]
            else:
                result.append([0]*(i+1))
                result[i][0],result[i][-1] = 1,1
                for j in range(1,i):
                    result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result