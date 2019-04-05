class LadderLength:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        if endWord not in wordList: return 0
        n, visited, wordSet = len(beginWord), set(), set(wordList)
        begin_set, end_set = {beginWord}, {endWord}
        level = 1 # begin word
        while begin_set and end_set:
            level += 1
            nextLayer = set()
            for word in begin_set:
                for i in range(n):
                    prefix, suffix = word[:i], word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nextWord = prefix + c + suffix
                        if nextWord in end_set: return level
                        if nextWord in wordSet and nextWord not in visited:
                            visited.add(nextWord)
                            nextLayer.add(nextWord)
            begin_set = nextLayer
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
        return 0

    def ladderLength3(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:
        if endWord not in wordList: return 0
        n, wordSet = len(beginWord), set(wordList)
        visited, queue = set([beginWord]), [(beginWord, 1)] # (word, level)
        while queue:
            for _ in range(len(queue)):
                word, level = queue.pop(0)
                for i in range(n):
                    prefix, postfix = word[:i], word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nextWord = prefix + c + postfix
                        if nextWord == endWord:
                            return level + 1
                        if nextWord in wordSet and nextWord not in visited:
                            visited.add(nextWord)
                            queue.append((nextWord, level + 1))
        return 0
