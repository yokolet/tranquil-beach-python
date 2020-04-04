from collections import defaultdict

class SentenceSimilarityTransitive:
    def areSentencesSimilarTwo(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        def find(w):
            if w not in group:
                group[w] = w
                return w
            while w != group[w]:
                w = group[group[w]]
            return w
        if len(words1) != len(words2): return False
        group = {}
        for p1, p2 in pairs:
            x, y = find(p1), find(p2)
            if x != y:
                group[y] = x
        for w1, w2 in zip(words1, words2):
            if find(w1) != find(w2): return False
        return True

    def areSentencesSimilarTwo2(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        def traverse(s, d):
            seen = {s}
            queue = [s]
            while queue:
                c = queue.pop(0)
                if d in p_dict[c]: return True
                for t in list(p_dict[c]):
                    if t not in seen:
                        seen.add(t)
                        queue.append(t)
            return False

        if len(words1) != len(words2): return False
        p_dict = defaultdict(set)
        for p1, p2 in pairs:
            p_dict[p1].add(p2)
            p_dict[p2].add(p1)
        for i in range(len(words1)):
            if words1[i] == words2[i] or \
                (words1[i] in p_dict and traverse(words1[i], words2[i])):
                continue
            return False
        return True
        