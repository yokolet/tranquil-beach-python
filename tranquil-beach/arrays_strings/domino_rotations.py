from collections import Counter

class DominoRotations:
    def minDominoRotations(self, A: 'List[int]', B: 'List[int]') -> int:
        n = len(A)
        count = Counter(A + B)
        if count.most_common(1)[0][1] < n:
            return -1
        v = count.most_common(1)[0][0]
        cnt_a, cnt_b = 0, 0
        for i in range(n):
            if A[i] != v and B[i] != v: return -1
            elif A[i] != v and B[i] == v:
                cnt_a += 1
            elif A[i] == v and B[i] != v:
                cnt_b += 1
        return min(cnt_a, cnt_b)

    def minDominoRotations1(self, A: 'List[int]', B: 'List[int]') -> int:
        def checkOneRow(a, b, v, count):
            for i in range(1, len(a)):
                if a[i] == v: continue
                elif b[i] == v:
                    count += 1
                else:
                    return -1
            return count

        result = []
        result.append(checkOneRow(A, B, A[0], 0))
        result.append(checkOneRow(A, B, B[0], 1))
        result.append(checkOneRow(B, A, A[0], 1))
        result.append(checkOneRow(B, A, B[0], 0))
        result = [v for v in result if v != -1]
        return min(result) if len(result) > 0 else -1

    def minDominoRotations2(self, A: 'List[int]', B: 'List[int]') -> int:
        n = len(A)
        count = Counter(A + B)
        if count.most_common(1)[0][1] < n:
            return -1
        target = count.most_common(1)[0][0]
        a_swap = 0
        b_swap = 0
        for i in range(n):
            if A[i] == B[i]:
                if A[i] == target:
                    continue
                else:
                    return -1
            elif A[i] == target:
                b_swap += 1
            elif B[i] == target:
                a_swap += 1
            else:
                return -1
        return min(a_swap, b_swap)
