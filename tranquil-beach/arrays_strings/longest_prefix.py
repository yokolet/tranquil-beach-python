class LongestPrefix:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        if not strs: return ''
        n = len(strs)
        prefix = min(strs, key=len)
        while prefix and sum([w[:len(prefix)]==prefix for w in strs]) != n:
            prefix = prefix[:-1]
        return prefix

    def longestCommonPrefix2(self, strs: 'List[str]') -> str:
        if not strs: return ''
        strs.sort(key=lambda x: len(x))
        prefix = strs[0]
        for w in strs[1:]:
            idx = 0
            while idx < len(prefix) and prefix[idx]==w[idx]:
                idx += 1
            prefix = prefix[:idx]
        return prefix
