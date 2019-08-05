class FlowerPlanting:
    def gardenNoAdj(self, N: int, paths: 'List[List[int]]') -> 'List[int]':
        g = {i: [] for i in range(N+1)}
        for s, d in paths:
            g[s].append(d)
            g[d].append(s)
        flowers = [0 for i in range(N+1)]
        all_flowers = {1, 2, 3, 4}
        for i in range(1, N+1):
            illegals = {flowers[n] for n in g[i]}
            flowers[i] = (all_flowers - illegals).pop()
        return flowers[1:]
