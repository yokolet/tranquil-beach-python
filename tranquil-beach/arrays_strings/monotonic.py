class Monotonic:
    def isMonotonic(self, A: 'List[int]') -> bool:
        if A[0] <= A[-1]: factor = 1
        else: factor = -1
        prev = A[0]
        for cur in A[1:]:
            if (cur - prev)*factor < 0:
                return False
            prev = cur
        return True

    def isMonotonic2(self, A: 'List[int]') -> bool:        
        if A[0] <= A[-1]:
            left = A[0]
            for x in A:
                if x >= left:
                    left = x
                else:
                    return False
        else:
            left = A[0]
            for x in A:
                if x <= left:
                    left = x
                else:
                    return False
        
        return True