from collections import defaultdict

class WordSquares:
    def wordSquares(self, words: 'List[str]') -> 'List[List[str]]':
        def prefixMap():
            d = defaultdict(set)
            for w in words:
                for p in [w[:i] for i in range(1, n)]:
                    d[p].add(w)
            return d

        def backtrack(idx, sub):
            if idx == n:
                result.append(sub[:])
                return
            prefix = ''.join([w[idx] for w in sub])
            if prefix not in prefix_dict: return
            for w in prefix_dict[prefix]:
                sub.append(w)
                backtrack(idx+1, sub)
                sub.pop()
        
        n = len(words[0])
        prefix_dict = prefixMap()
        result = []
        for w in words:
            backtrack(1, [w])
        return result
