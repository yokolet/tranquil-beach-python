from collections import defaultdict

class SmallestCharacter:
    def numSmallerByFrequency(self, queries: 'List[str]', words: 'List[str]') -> 'List[int]':
        def counter(w):
            return w.count(min(w))
        w_freq = defaultdict(int)
        for w in words:
            w_freq[counter(w)] += 1
        w_values = sorted(w_freq.keys(), reverse=True)
        result = []
        for q in queries:
            q_freq = counter(q)
            cnt = 0
            for w_val in w_values:
                if w_val > q_freq: cnt += w_freq[w_val]
                else: break
            result.append(cnt)
        return result
            