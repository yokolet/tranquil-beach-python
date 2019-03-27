from collections import Counter, defaultdict
import heapq

class TopWords:
    def topKFrequent(self, words: 'List[str]', k: int) -> 'List[str]':
        counts = defaultdict(int)
        for w in words:
            counts[w] += 1
        freq = [(-v, word) for word, v in counts.items()]
        heapq.heapify(freq)
        return [heapq.heappop(freq)[1] for _ in range(k)]

    def topKFrequent2(self, words: 'List[str]', k: int) -> 'List[str]':
        cnt = defaultdict(int)
        for w in  words:
            cnt[w] += 1
        
        pairs = []
        for key, value in  cnt.items():
            pairs.append((value, key))
        
        pairs.sort(key=lambda t: t[1])
        pairs.sort(key=lambda t: t[0], reverse=True)
        
        res = []
        for i in range(k):
            res.append(pairs[i][1])
            
        return res    