from collections import defaultdict

class StoneRemoving:
    def removeStones(self, stones: 'List[List[int]]') -> int:
        n = len(stones)
        groups = [i for i in range(n)]
        rows = defaultdict(list)
        cols = defaultdict(list)

        def find(p):
            while p != groups[p]:
                p = groups[p]
            return p
        
        def union(m):
            count = 0
            for _, indices in m.items():
                parent = min(indices)
                x = find(parent)
                for idx in indices:
                    y = find(idx)
                    if x != y:
                        groups[y] = x
                        count += 1
            return count

        for i in range(n):
            r, c = stones[i]
            rows[r].append(i)
            cols[c].append(i)
        
        return union(rows) + union(cols)
