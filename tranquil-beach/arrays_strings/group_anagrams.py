class GroupAnagrams:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return [v for _, v in groups.items()]