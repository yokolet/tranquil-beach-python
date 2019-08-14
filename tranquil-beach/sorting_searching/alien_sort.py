class AlienSort:
    def isAlienSorted(self, words: 'List[str]', order: str) -> bool:
        memo = {c: i for i, c in enumerate(order)}
        prev = words[0]
        for cur in words[1:]:
            i, j = 0, 0
            while i < len(prev) and j < len(cur) and prev[i] == cur[j]:
                i += 1
                j += 1
            if i < len(prev) and j < len(cur) and memo[prev[i]] > memo[cur[j]]:
                return False
            if len(prev) > len(cur) and prev[i-1] == cur[j-1]:
                return False
            prev = cur
        return True


    def isAlienSorted2(self, words: 'List[str]', order: str) -> bool:
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

    def isAlienSorted3(self, words: 'List[str]', order: str) -> bool:
        order_map={c:i for i,c in enumerate(order)}  # create a hashmap
        wordIndices=[[order_map[c] for c in word] for word in words]
        return all(w1<=w2 for w1,w2 in zip(wordIndices,wordIndices[1:]))
