from collections import defaultdict

class SentenceSimilarity:
    def areSentencesSimilar(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2): return False
        p_dict = defaultdict(set)
        for p1, p2 in pairs:
            p_dict[p1].add(p2)
            p_dict[p2].add(p1)
        for i in range(len(words1)):
            if words1[i] == words2[i] or\
                (words1[i] in p_dict and words2[i] in p_dict[words1[i]]):
                continue
            return False
        return True
