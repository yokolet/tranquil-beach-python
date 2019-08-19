class IntervalIntersection:
    def intervalIntersection(self, A: 'List[List[int]]', B: 'List[List[int]]') -> 'List[List[int]]':
        if not A or not B: return []
        i, j, result = 0, 0, []
        while i < len(A) and j < len(B):
            cur_a, cur_b = A[i], B[j]
            start, end = max(cur_a[0], cur_b[0]), min(cur_a[1], cur_b[1])
            if start <= end:
                result.append([start, end])
            if cur_a[1] == cur_b[1]:
                i += 1
                j += 1
            elif cur_a[1] < cur_b[1]:
                i += 1
            else:
                j += 1
        return result
