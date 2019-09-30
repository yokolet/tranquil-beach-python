import bisect

class OddEvenJump:
    def oddEvenJumps(self, A: 'List[int]') -> 'int':
        n = len(A)

        def makeNext(indices):
            result = [None for _ in range(len(indices))]
            stack = []
            for i in indices:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        a = [(v, i) for i, v in enumerate(A)]
        indices = [i for _, i in sorted(a, key=lambda x: x[0])]
        next_odd = makeNext(indices)
        indices = [i for _, i in sorted(a, key=lambda x: x[0], reverse=True)]
        next_even = makeNext(indices)

        odds, evens = [False for _ in range(n)], [False for _ in range(n)]
        odds[-1], evens[-1] = True, True

        for i in range(n-2, -1, -1):
            if next_odd[i] is not None:
                odds[i] = evens[next_odd[i]]
            if next_even[i] is not None:
                evens[i] = odds[next_even[i]]
        return sum(odds)

    def oddEvenJumps2(self, A: 'List[int]') -> int:
        n = len(A)
        memo, values = {A[-1]: [1, 1]}, [A[-1]]
        result = 1 
        for i in range(n-2, -1, -1):
            idx = bisect.bisect_left(values, A[i])
            if 0 <= idx < len(values) and values[idx] in memo:
                even = memo[values[idx]][0]
                if even:
                    result += 1
            else:
                even = False
            idx = bisect.bisect_right(values, A[i])
            if 0 <= idx-1 < len(values) and values[idx-1] in memo:
                odd = memo[values[idx-1]][1]
            else:
                odd = False
            memo[A[i]] = [odd, even]
            values.insert(idx, A[i])
        return result
