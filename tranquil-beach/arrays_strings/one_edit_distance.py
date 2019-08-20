class OneEditDistance:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        seen = set()
        queue = [(s, t, 0)]
        while queue:
            w1, w2, d = queue.pop(0)
            if d > 1: return False
            if w1 == w2:
                if d == 1: return True
                else: return False
            if (w1, w2) in seen:
                continue
            seen.add((w1, w2))
            while w1 and w2 and w1[0] == w2[0]:
                w1 = w1[1:]
                w2 = w2[1:]
            queue.append((w1, w2[1:], d+1))
            queue.append((w1[1:], w2, d+1))
            queue.append((w1[1:], w2[1:], d+1))
