from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(set) # {word_length: set of words}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.table[len(word)].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        length = len(word)
        if length not in self.table: return False
        if word in self.table[length]: return True
        tmp = self.table[length]
        for i in range(length):
            if word[i] == '.':
                continue
            tmp = {c for c in tmp if c[i] == word[i]}
            if not tmp: return False
        return True
