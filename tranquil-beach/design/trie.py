class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.marker = '$'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.children
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[self.marker] = None

    def __search__(self, word: str) -> bool:
        cur = self.children
        for c in word:
            if c not in cur: return False
            cur = cur[c]
        return True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.__search__(word + self.marker)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.__search__(prefix)
