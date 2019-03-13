class AlienSort:
    def isAlienSorted(self, words: 'List[str]', order: str) -> bool:
        memo = {}
        for i, c in enumerate(order):
            memo[c] = i
        prev = words[0]
        for cur in words[1:]:
            i, j, sub = 0, 0, True
            while i < len(prev) and j < len(cur):
                if memo[prev[i]] > memo[cur[j]]:
                    return False
                if memo[prev[i]] < memo[cur[j]]:
                    sub = False
                    break
                i += 1
                j += 1
            if len(cur) < len(prev) and sub:
                return False
            prev = cur
        return True
