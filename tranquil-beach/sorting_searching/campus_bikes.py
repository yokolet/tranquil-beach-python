class CampusBikes:
    def assignBikes(self, workers: 'List[List[int]]', bikes: 'List[List[int]]') -> 'List[int]':
        memo = [[] for _ in range(2001)]
        dist = lambda x, y: abs(x[0]-y[0])+abs(x[1]-y[1])
        for i in range(len(workers)):
            for j in range(len(bikes)):
                memo[(dist(workers[i], bikes[j]))].append((i, j))

        ans, used = [None for i in range(len(workers))], set()
        for d in range(2001):
            for w, b in memo[d]:
                if ans[w] is None and b not in used:
                    ans[w] = b
                    used.add(b)
        return ans
