from collections import defaultdict, Counter

class TopK:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        counts = Counter(nums).most_common(k)
        return [k for k, _ in counts]

    def topKFrequent3(self, nums: 'List[int]', k: int) -> 'List[int]':
        counts = defaultdict(int)
        for v in nums:
            counts[v] += 1
        freq = []
        for key, val in counts.items():
            freq.append([key, val])
        freq = sorted(freq, key=lambda x: x[1], reverse=True)[:k]
        return [key for key, _ in freq]


