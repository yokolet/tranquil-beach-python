class PalindromePairs:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        revWords = {w[::-1]: i for i, w in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                if prefix in revWords and\
                    revWords[prefix] != i and\
                    suffix == suffix[::-1]:
                    result.append([i, revWords[prefix]])
                if j > 0 and\
                    suffix in revWords and\
                    revWords[suffix] != i and\
                    prefix == prefix[::-1]:
                    result.append([revWords[suffix], i])
        return result
