from collections import defaultdict

class GroupAnagrams:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        groups = defaultdict(list)
        for s in strs:
            h = 0
            for c in s:
                h += hash(c)
            groups[h].append(s)
        return [v for v in groups.values()]

    def groupAnagrams2(self, strs: 'List[str]') -> 'List[List[str]]':
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return [v for _, v in groups.items()]